# YouTube Video Downloader API

This is a Flask-based web API that converts the original `main.py` YouTube downloader script into a web service.

## API Endpoints

### Health Check
```
GET /health
```
Returns the API status.

### List Available Formats
```
GET /api/list?url={youtube_url}
POST /api/list
Content-Type: application/json
{
    "url": "{youtube_url}"
}
```
Returns available video formats with their quality and format IDs.

### Download Video
```
POST /api/download
Content-Type: application/json
{
    "url": "{youtube_url}",
    "format_index": {format_index_number},
    "output_dir": "{optional_output_directory}"
}
```
Downloads the video in the specified format and returns the filename.

### Access Downloaded Files
```
GET /files/{filename}
```
Downloads the specified file from the upload directory.

## File Structure

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `test_api.py` - API test script
- `now/upload/` - Directory where downloaded files are stored (created automatically)

## Running the API

### Local Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
python app.py
```

3. The API will be available at `http://localhost:5000`

### Docker Installation

1. Build the Docker image:
```bash
docker build -t youtube-downloader-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 -v $(pwd)/now/upload:/app/now/upload youtube-downloader-api
```

3. The API will be available at `http://localhost:5000`

Note: The volume mount ensures downloaded files persist between container restarts.

## Usage Example

1. First, list available formats:
```bash
curl -X POST http://localhost:5000/api/list -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

2. Then download using a format index:
```bash
curl -X POST http://localhost:5000/api/download -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "format_index": 0}'
```

3. Access the downloaded file:
```bash
curl http://localhost:5000/files/{filename}
```

## Docker Support

The upload directory is dynamically set to `now/upload` relative to the current working directory, making it compatible with Docker containers.
