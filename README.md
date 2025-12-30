# WhatsApp Video Sender API

A Node.js application for sending videos to WhatsApp using direct URLs with optional audio merging using FFmpeg.

## Features

- Send videos directly from URLs to WhatsApp contacts/groups
- Merge video and audio tracks using FFmpeg
- Automatic file size detection and appropriate sending method (video vs document)
- QR code authentication for WhatsApp connection
- Automatic reconnection on connection loss
- Comprehensive error handling and logging
- Health check endpoint
- API documentation endpoint

## Prerequisites

- Node.js 18+
- FFmpeg (for audio merging)
- Docker (for containerized deployment)

## Installation

### Local Installation

```bash
# Clone the repository (if applicable)
git clone https://github.com/your-repo/whatsapp-video-sender.git
cd whatsapp-video-sender

# Install dependencies
npm install

# Start the application
node index.js
```

### Docker Installation

```bash
# Build the Docker image
docker build -t whatsapp-video-sender .

# Run the container
docker run -d -p 5000:5000 --name whatsapp-video-sender whatsapp-video-sender
```

## Configuration

The application can be configured using environment variables or by modifying the `CONFIG` object in `index.js`:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Port to run the server on |
| `TEMP_DIR` | /tmp/whatsapp-videos/ | Directory for temporary files |
| `MAX_VIDEO_SIZE_MB` | 100 | Maximum file size for video sending (MB) |
| `MAX_DOCUMENT_SIZE_MB` | 2000 | Maximum file size for document sending (MB) |
| `LOG_LEVEL` | silent | Logging level (silent, debug, etc.) |
| `DOWNLOAD_TIMEOUT` | 300000 | Download timeout in milliseconds |
| `FFMPEG_TIMEOUT` | 600000 | FFmpeg processing timeout in milliseconds |

## API Endpoints

### POST /api/send-video-url

Send a video to WhatsApp from a direct URL.

**Request Body:**

```json
{
  "type": "direct",
  "video_url": "https://example.com/video.mp4",
  "chat_id": "923164525711@s.whatsapp.net",
  "caption": "Check this video!",
  "filename": "my-video.mp4"
}
```

**Response:**

```json
{
  "success": true,
  "message": "Video sent successfully",
  "data": {
    "messageId": "1234567890",
    "chatId": "923164525711@s.whatsapp.net",
    "fileName": "my-video.mp4",
    "fileSize": "10.25 MB",
    "fileSizeMB": 10.25,
    "processType": "direct",
    "sentAs": "video",
    "reason": "File size (10.25 MB) is under 100 MB",
    "caption": "Check this video!",
    "timestamp": "2023-12-30T08:32:07.123Z",
    "processingTimeMs": 1500,
    "processingTimeSec": 1.5
  }
}
```

### GET /api/health

Check the health status of the API and FFmpeg availability.

**Response:**

```json
{
  "success": true,
  "status": "connected",
  "whatsapp": {
    "connected": true,
    "user": {
      "id": "923164525711@s.whatsapp.net"
    }
  },
  "system": {
    "ffmpeg": true,
    "tempDir": "/tmp/whatsapp-videos/",
    "maxVideoSizeMB": 100,
    "maxDocumentSizeMB": 2000
  },
  "uptime": 1234.56,
  "timestamp": "2023-12-30T08:32:07.123Z"
}
```

### GET /api/docs

Get API documentation and examples.

## Usage Examples

### Direct Video Send

```bash
curl -X POST http://localhost:5000/api/send-video-url \
  -H "Content-Type: application/json" \
  -d '{
    "type": "direct",
    "video_url": "https://example.com/video.mp4",
    "chat_id": "923164525711@s.whatsapp.net",
    "caption": "Check this out!",
    "filename": "video.mp4"
  }'
```

### Video + Audio Merge

```bash
curl -X POST http://localhost:5000/api/send-video-url \
  -H "Content-Type: application/json" \
  -d '{
    "type": "merge",
    "video_url": "https://example.com/video.mp4",
    "audio_url": "https://example.com/audio.mp3",
    "chat_id": "923164525711@s.whatsapp.net",
    "caption": "High quality video!",
    "filename": "merged-video.mp4"
  }'
```

## Chat ID Formats

The application supports various WhatsApp chat ID formats:

- Individual chats: `923164525711@s.whatsapp.net`
- Group chats: `120363424911005190@g.us`
- Broadcast lists: `123456789@broadcast`

Note: The application automatically normalizes `@c.us` format to `@s.whatsapp.net`.

## Error Handling

The API provides comprehensive error responses with specific error codes:

- `NOT_CONNECTED`: WhatsApp not connected
- `MISSING_FIELDS`: Required fields missing
- `INVALID_CHATID`: Invalid chat ID format
- `DOWNLOAD_FAILED`: File download failed
- `FFMPEG_FAILED`: FFmpeg processing failed
- `FILE_TOO_LARGE`: File exceeds size limits
- `SEND_FAILED`: Failed to send message
- `INTERNAL_ERROR`: Internal server error

## Docker Deployment

### Building the Image

```bash
docker build -t whatsapp-video-sender .
```

### Running the Container

```bash
docker run -d \
  -p 5000:5000 \
  --name whatsapp-video-sender \
  -v /path/to/auth_info_baileys:/app/auth_info_baileys \
  whatsapp-video-sender
```

### Environment Variables

You can override configuration using environment variables:

```bash
docker run -d \
  -p 5000:5000 \
  --name whatsapp-video-sender \
  -e PORT=3000 \
  -e MAX_VIDEO_SIZE_MB=150 \
  whatsapp-video-sender
```

## Development

### Running Locally

```bash
# Install dependencies
npm install

# Start the server
node index.js
```

### Testing

The application includes basic error handling and validation. You can test the API using:

- Postman
- cURL
- Any HTTP client

## Troubleshooting

### FFmpeg Not Found

Ensure FFmpeg is installed and available in your system PATH. For Docker, it's included in the image.

### Connection Issues

- Check your internet connection
- Verify WhatsApp credentials
- Check the QR code scanning process

### File Size Limits

- Videos under 100MB are sent as videos
- Larger files are sent as documents
- Maximum file size is 2000MB (2GB)

## License

MIT
