#!/usr/bin/env python3
import yt_dlp
import json
import math
import random
import shutil
import sys
import time
import os
from typing import List, Dict, Optional
from flask import Flask, request, jsonify, send_from_directory, abort

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
ALLOWED_EXTENSIONS = {'mp4', 'webm', 'mkv', 'avi', 'mov'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ----- Helpers -----

def has_ffmpeg() -> bool:
    return shutil.which("ffmpeg") is not None

def output_error(msg: str, code: int = 400):
    return jsonify({"status": "error", "message": msg}), code

def output_ok(obj: Dict):
    return jsonify(obj), 200

def fetch_info(url: str) -> Dict:
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as y:
        return y.extract_info(url, download=False)

def categorize(fmts: List[Dict]):
    prog, audio, video = [], [], []
    for f in fmts:
        v = f.get('vcodec'); a = f.get('acodec')
        if v not in (None, 'none') and a not in (None, 'none'):
            prog.append(f)
        elif v not in (None, 'none'):
            video.append(f)
        elif a not in (None, 'none'):
            audio.append(f)
    return prog, audio, video

# ----- List Formats Endpoint -----

@app.route('/api/list', methods=['GET', 'POST'])
def api_list():
    data = request.get_json() if request.is_json else request.form
    url = data.get('url') if data else request.args.get('url')

    if not url:
        return output_error("URL parameter is required")

    try:
        info = fetch_info(url)
    except Exception as e:
        return output_error(f"failed_fetch_info: {str(e)}")

    prog, audio, video = categorize(info.get("formats", []))
    results = []
    idx = 0

    for f in sorted(prog, key=lambda x: (x.get('height') or 0), reverse=True):
        results.append({
            "index": idx,
            "type": "progressive",
            "quality": f"{f.get('height')}p",
            "format_id": f.get('format_id')
        })
        idx += 1

    best_vid = sorted(video, key=lambda x: (x.get('height') or 0), reverse=True)
    best_aud = sorted(audio, key=lambda x: (x.get('abr') or 0), reverse=True)

    for v in best_vid[:3]:
        for a in best_aud[:2]:
            results.append({
                "index": idx,
                "type": "merge",
                "video_quality": f"{v.get('height')}p",
                "audio_rate": f"{int(a.get('abr') or 0)}kbps",
                "v_id": v.get('format_id'),
                "a_id": a.get('format_id')
            })
            idx += 1

    return output_ok({
        "status": "ok",
        "video_id": info.get("id"),
        "title": info.get("title"),
        "formats": results
    })

# ----- Download Endpoint -----

@app.route('/api/download', methods=['POST'])
def api_download():
    data = request.get_json() if request.is_json else request.form
    url = data.get('url')
    format_index = data.get('format_index')
    output_dir = data.get('output_dir', app.config['UPLOAD_FOLDER'])

    if not url or format_index is None:
        return output_error("URL and format_index parameters are required")

    try:
        format_index = int(format_index)
    except ValueError:
        return output_error("format_index must be an integer")

    try:
        info = fetch_info(url)
    except Exception as e:
        return output_error(f"failed_fetch_info: {str(e)}")

    prog, audio, video = categorize(info.get("formats", []))
    all_list = []

    for f in sorted(prog, key=lambda x: (x.get('height') or 0), reverse=True):
        all_list.append(("prog", f))

    best_vid = sorted(video, key=lambda x: (x.get('height') or 0), reverse=True)
    best_aud = sorted(audio, key=lambda x: (x.get('abr') or 0), reverse=True)

    for v in best_vid[:3]:
        for a in best_aud[:2]:
            all_list.append(("merge", (v, a)))

    if format_index < 0 or format_index >= len(all_list):
        return output_error("invalid_format_index")

    mode, sel = all_list[format_index]

    # create safe filename: <timestamp>_<random>
    safe_name = f"{int(time.time())}_{random.randint(1000,9999)}"
    outtmpl = f"{output_dir}/{safe_name}.%(ext)s"

    ydl_opts = {
        "outtmpl": outtmpl,
        "restrictfilenames": True,
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
    }

    try:
        if mode == "prog":
            ydl_opts["format"] = sel.get("format_id")
            with yt_dlp.YoutubeDL(ydl_opts) as y:
                y.download([url])
        else:
            if not has_ffmpeg():
                return output_error("ffmpeg_required")
            v, a = sel
            combo = f"{v.get('format_id')}+{a.get('format_id')}"
            ydl_opts["format"] = combo
            ydl_opts["merge_output_format"] = "mp4"
            with yt_dlp.YoutubeDL(ydl_opts) as y:
                y.download([url])
    except Exception as e:
        return output_error(f"download_failed: {str(e)}")

    # final saved file
    saved_file = f"{output_dir}/{safe_name}.mp4"

    # Check if file exists and return the filename
    if os.path.exists(saved_file):
        filename = os.path.basename(saved_file)
        return output_ok({"status": "ok", "file": filename})
    else:
        return output_error("download_failed: file not created")

# ----- File Access Endpoint -----

@app.route('/files/<filename>', methods=['GET'])
def serve_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# ----- Health Check Endpoint -----

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API is running"})

if __name__ == "__main__":
    # Create upload directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
