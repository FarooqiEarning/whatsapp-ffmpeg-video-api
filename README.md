# 🚀 WhatsApp Video Sender API

**A Product of Converso Empire** - Revolutionizing Digital Communication

![Converso Empire Banner](https://via.placeholder.com/800x200/007BFF/FFFFFF?text=Converso+Empire:+Building+the+Future)

> "Empowering businesses and individuals with cutting-edge WhatsApp automation technology"

**🏛️ Converso Empire: Where Innovation Meets Communication**

Welcome to the future of WhatsApp video messaging! This powerful API, proudly developed by Converso Empire, enables seamless video delivery directly from URLs to WhatsApp contacts and groups, with advanced features like audio merging, intelligent file handling, and robust error management.

## 🌟 Key Features

✅ **Direct URL Video Sending** - Send videos to WhatsApp without downloading to your server
✅ **Advanced Audio Merging** - Combine video and audio tracks using FFmpeg for professional results
✅ **Smart File Handling** - Automatic detection of optimal sending method based on file size
✅ **QR Code Authentication** - Secure and easy WhatsApp connection setup
✅ **Auto-Reconnection** - Never lose connection with automatic reconnection capabilities
✅ **Enterprise-Grade Error Handling** - Comprehensive error management and detailed logging
✅ **Health Monitoring** - Built-in health check endpoint for system monitoring
✅ **Complete API Documentation** - Full API reference with examples and best practices
✅ **Production-Ready** - Built for scalability, reliability, and performance

## 🎯 Use Cases

🔹 **Business Automation** - Automate video marketing campaigns via WhatsApp
🔹 **Content Distribution** - Deliver video content to subscribers and customers
🔹 **Customer Support** - Send tutorial and help videos instantly
🔹 **Media Sharing** - Share video content with friends, family, and groups
🔹 **Educational Platforms** - Distribute course videos and educational content
🔹 **Social Media Integration** - Cross-platform video sharing solutions

## 📋 System Requirements

For optimal performance, ensure your system meets these requirements:

| Component | Requirement | Notes |
|-----------|------------|-------|
| **Docker** | Docker Engine 20.10+ | Required for containerized deployment |
| **Docker Compose** | Version 1.29+ | For simplified deployment |
| **Operating System** | Linux, Windows, macOS | Cross-platform compatible |
| **CPU** | 2+ cores recommended | For smooth video processing |
| **RAM** | 4GB+ recommended | For handling multiple requests |
| **Storage** | 10GB+ available space | For temporary video files |
| **Network** | Stable internet connection | Required for WhatsApp connectivity |

## 🚀 Installation & Deployment

**💡 Pro Tip:** We recommend using Docker for the easiest and most reliable deployment experience.

### ✅ Docker Compose Deployment (Recommended)

The fastest way to get started with our WhatsApp Video Sender API:

```bash
# Step 1: Clone the official Converso Empire repository
git clone https://github.com/Converso-Empire/whatsapp-ffmpeg-video-api.git
cd whatsapp-ffmpeg-video-api

# Step 2: Start the application with Docker Compose
docker compose up -d

# Step 3: Verify the service is running
docker compose ps

# Step 4: Check application health
curl http://localhost:5000/api/health
```

**What happens during deployment:**
- ✅ Automatically pulls the latest `Converso-Empire/whatsapp-ffmpeg-video-api` image
- ✅ Sets up persistent volumes for authentication and temporary files
- ✅ Configures all necessary environment variables with optimal defaults
- ✅ Starts the service with built-in health monitoring
- ✅ Enables automatic restart on failures

### 🛠️ Advanced Deployment Options

#### Custom Configuration

Override default settings using environment variables:

```bash
# Create a custom .env file
echo "PORT=3000" > .env
echo "MAX_VIDEO_SIZE_MB=150" >> .env
echo "LOG_LEVEL=debug" >> .env

# Start with custom configuration
docker compose --env-file .env up -d
```

#### Production Deployment

For production environments, we recommend:

```bash
# Use production-optimized settings
docker compose up -d

# Set up monitoring and logging
docker compose logs -f

# Configure automatic updates (optional)
watchtower --interval 30 --cleanup
```

#### Scaling for High Traffic

```bash
# Scale to multiple instances (requires load balancer)
docker compose up -d --scale whatsapp-video-api=3

# Use with reverse proxy (Nginx example)
location /whatsapp-api/ {
    proxy_pass http://localhost:5000/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### 🔧 Manual Docker Deployment

For users who prefer manual control:

```bash
# Build the Docker image
docker build -t whatsapp-video-sender .

# Run the container with custom settings
docker run -d \
  -p 5000:5000 \
  --name whatsapp-video-sender \
  -v $(pwd)/auth_data:/app/auth_info_baileys \
  -v $(pwd)/temp_files:/tmp/whatsapp-videos \
  -e PORT=5000 \
  -e MAX_VIDEO_SIZE_MB=120 \
  -e LOG_LEVEL=info \
  --restart unless-stopped \
  whatsapp-video-sender
```

## ⚙️ Advanced Configuration

**💡 Configuration Philosophy:** Our API is designed with flexibility in mind, allowing you to fine-tune every aspect of the video sending process.

### Environment Variables

Configure the application using environment variables for maximum flexibility:

| Variable | Default | Description | Recommended Range |
|----------|---------|-------------|-------------------|
| `PORT` | 5000 | Server port | 1024-65535 |
| `TEMP_DIR` | /tmp/whatsapp-videos/ | Temporary file storage | Any writable directory |
| `MAX_VIDEO_SIZE_MB` | 100 | Max video file size | 50-200 MB |
| `MAX_DOCUMENT_SIZE_MB` | 2000 | Max document file size | 500-5000 MB |
| `LOG_LEVEL` | info | Logging verbosity | silent, error, warn, info, debug |
| `DOWNLOAD_TIMEOUT` | 300000 | Download timeout (ms) | 60000-600000 |
| `FFMPEG_TIMEOUT` | 600000 | FFmpeg processing timeout (ms) | 300000-1200000 |
| `AUTO_RECONNECT` | true | Auto-reconnect on failure | true/false |
| `QR_REFRESH_INTERVAL` | 30000 | QR code refresh interval (ms) | 10000-60000 |
| `MAX_CONCURRENT_DOWNLOADS` | 5 | Concurrent download limit | 1-20 |

### Configuration Best Practices

```bash
# Development environment (verbose logging)
docker run -e LOG_LEVEL=debug -e MAX_VIDEO_SIZE_MB=50 ...

# Production environment (optimized performance)
docker run -e LOG_LEVEL=warn -e MAX_CONCURRENT_DOWNLOADS=10 ...

# High-traffic environment (scalability)
docker run -e DOWNLOAD_TIMEOUT=600000 -e FFMPEG_TIMEOUT=900000 ...
```

### Configuration Files

For complex setups, use configuration files:

```yaml
# config.yaml example
server:
  port: 5000
  logLevel: info

whatsapp:
  autoReconnect: true
  qrRefreshInterval: 30000

fileHandling:
  tempDir: /app/temp_videos
  maxVideoSizeMB: 100
  maxDocumentSizeMB: 2000

performance:
  maxConcurrentDownloads: 5
  downloadTimeout: 300000
  ffmpegTimeout: 600000
```

**📊 Performance Tuning Tips:**
- Increase `MAX_CONCURRENT_DOWNLOADS` for high-volume environments
- Adjust timeouts based on your network conditions
- Monitor resource usage and scale accordingly
- Use separate volumes for better I/O performance

## 🔌 API Reference

**📘 API Design Philosophy:** Our API follows RESTful principles with JSON payloads, designed for simplicity, consistency, and developer productivity.

### 📤 POST /api/send-video-url

**The heart of our API** - Send videos to WhatsApp with powerful options

**Request Body Parameters:**

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `type` | string | ✅ Yes | Operation type: "direct" or "merge" | "direct" |
| `video_url` | string | ✅ Yes | Direct URL to video file | "https://example.com/video.mp4" |
| `chat_id` | string | ✅ Yes | WhatsApp chat ID | "923164525711@s.whatsapp.net" |
| `caption` | string | ❌ No | Message caption | "Check this amazing video!" |
| `filename` | string | ❌ No | Custom filename | "my-video.mp4" |
| `audio_url` | string | ❌ No (required for "merge") | URL to audio file | "https://example.com/audio.mp3" |
| `priority` | string | ❌ No | Processing priority | "high", "normal", "low" |
| `retry_on_failure` | boolean | ❌ No | Auto-retry failed sends | true |

**Request Examples:**

```json
{
  "type": "direct",
  "video_url": "https://example.com/video.mp4",
  "chat_id": "923164525711@s.whatsapp.net",
  "caption": "Check this video!",
  "filename": "my-video.mp4",
  "priority": "high"
}
```

```json
{
  "type": "merge",
  "video_url": "https://example.com/video.mp4",
  "audio_url": "https://example.com/audio.mp3",
  "chat_id": "120363424911005190@g.us",
  "caption": "Video with custom audio!",
  "filename": "merged-content.mp4",
  "retry_on_failure": true
}
```

**Response Structure:**

```json
{
  "success": true,
  "message": "Video sent successfully",
  "data": {
    "messageId": "1234567890ABCDEF",
    "chatId": "923164525711@s.whatsapp.net",
    "fileName": "my-video.mp4",
    "fileSize": "10.25 MB",
    "fileSizeMB": 10.25,
    "processType": "direct",
    "sentAs": "video",
    "reason": "File size (10.25 MB) is under 100 MB limit",
    "caption": "Check this video!",
    "timestamp": "2023-12-30T08:32:07.123Z",
    "processingTimeMs": 1500,
    "processingTimeSec": 1.5,
    "status": "delivered",
    "deliveryTimestamp": "2023-12-30T08:32:08.654Z"
  }
}
```

### 🩺 GET /api/health

**Comprehensive health monitoring endpoint**

```json
{
  "success": true,
  "status": "connected",
  "whatsapp": {
    "connected": true,
    "user": {
      "id": "923164525711@s.whatsapp.net",
      "name": "John Doe",
      "platform": "android"
    },
    "connectionUptime": 3600,
    "lastReconnect": "2023-12-30T07:32:07.123Z"
  },
  "system": {
    "ffmpeg": {
      "available": true,
      "version": "4.4.1",
      "supportedFormats": ["mp4", "mov", "avi", "mkv"]
    },
    "tempDir": "/tmp/whatsapp-videos/",
    "storage": {
      "available": "15.2 GB",
      "used": "2.8 GB"
    },
    "maxVideoSizeMB": 100,
    "maxDocumentSizeMB": 2000,
    "concurrentDownloads": 0,
    "activeProcesses": 2
  },
  "performance": {
    "uptime": 1234.56,
    "memoryUsage": "45%",
    "cpuUsage": "12%",
    "requestsProcessed": 42,
    "averageResponseTime": 850
  },
  "timestamp": "2023-12-30T08:32:07.123Z",
  "version": "2.0.0"
}
```

### 📚 GET /api/docs

**Interactive API documentation with live examples**

```json
{
  "api": "WhatsApp Video Sender API",
  "version": "2.0.0",
  "description": "Advanced WhatsApp video sending solution by Converso Empire",
  "endpoints": [
    {
      "path": "/api/send-video-url",
      "method": "POST",
      "description": "Send video to WhatsApp",
      "example": {
        "request": {
          "type": "direct",
          "video_url": "https://example.com/video.mp4",
          "chat_id": "923164525711@s.whatsapp.net"
        },
        "response": {
          "success": true,
          "message": "Video sent successfully"
        }
      }
    },
    {
      "path": "/api/health",
      "method": "GET",
      "description": "System health check"
    },
    {
      "path": "/api/docs",
      "method": "GET",
      "description": "API documentation"
    }
  ],
  "authentication": "None (local network only)",
  "rateLimits": "None (self-hosted)",
  "support": "support@conversoempire.com"
}
```

### 🔄 Webhook Integration (Coming Soon)

```json
{
  "webhookUrl": "https://your-server.com/webhook",
  "events": ["message_sent", "message_delivered", "message_failed"],
  "secret": "your-secret-key"
}
```

## 🎬 Practical Usage Examples

**💡 Real-world scenarios and best practices**

### 📱 Basic Video Send

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

### 🎵 Video + Audio Merge (Professional Quality)

```bash
curl -X POST http://localhost:5000/api/send-video-url \
  -H "Content-Type: application/json" \
  -d '{
    "type": "merge",
    "video_url": "https://example.com/video.mp4",
    "audio_url": "https://example.com/audio.mp3",
    "chat_id": "923164525711@s.whatsapp.net",
    "caption": "High quality video with custom audio!",
    "filename": "merged-video.mp4",
    "priority": "high"
  }'
```

### 📊 Bulk Video Distribution

```bash
# Using jq for JSON processing
for chat_id in $(cat contacts.txt); do
  curl -X POST http://localhost:5000/api/send-video-url \
    -H "Content-Type: application/json" \
    -d "{
      \"type\": \"direct\",
      \"video_url\": \"https://example.com/promo.mp4\",
      \"chat_id\": \"$chat_id\",
      \"caption\": \"Exclusive offer just for you!\",
      \"filename\": \"promo-video.mp4\"
    }"
done
```

### 🔄 Advanced Workflow with Error Handling

```bash
# Send video with retry logic
response=$(curl -s -X POST http://localhost:5000/api/send-video-url \
  -H "Content-Type: application/json" \
  -d '{
    "type": "direct",
    "video_url": "https://example.com/large-video.mp4",
    "chat_id": "120363424911005190@g.us",
    "caption": "Group video announcement",
    "filename": "announcement.mp4",
    "retry_on_failure": true
  }')

# Check response and handle errors
if echo "$response" | jq -e '.success == true' >/dev/null; then
  echo "Video sent successfully!"
  echo "$response" | jq '.data'
else
  echo "Failed to send video:"
  echo "$response" | jq '.error'
  # Implement fallback logic here
fi
```

### 📈 Monitoring and Analytics

```bash
# Health monitoring script
while true; do
  health=$(curl -s http://localhost:5000/api/health)
  status=$(echo "$health" | jq -r '.status')
  whatsapp_connected=$(echo "$health" | jq -r '.whatsapp.connected')
  uptime=$(echo "$health" | jq -r '.performance.uptime')

  echo "[$(date)] Status: $status | WhatsApp: $whatsapp_connected | Uptime: $uptime sec"

  if [ "$status" != "connected" ] || [ "$whatsapp_connected" = "false" ]; then
    # Alerting logic
    echo "ALERT: Service not healthy!" | mail -s "WhatsApp API Alert" admin@example.com
  fi

  sleep 60
done
```

### 🎯 Targeted Marketing Campaign

```bash
# Segmented video campaign
segments=(
  "new_customers:Welcome to our community! Here's your exclusive video guide."
  "loyal_customers:Thank you for your loyalty! Enjoy this special content."
  "inactive_customers:We miss you! Here's what you've been missing."
)

for segment in "${segments[@]}"; do
  IFS=':' read -r segment_name message <<< "$segment"
  video_url="https://example.com/videos/$segment_name.mp4"

  # Send to all contacts in segment
  while read -r chat_id; do
    curl -X POST http://localhost:5000/api/send-video-url \
      -H "Content-Type: application/json" \
      -d "{
        \"type\": \"direct\",
        \"video_url\": \"$video_url\",
        \"chat_id\": \"$chat_id\",
        \"caption\": \"$message\",
        \"filename\": \"$segment_name-video.mp4\",
        \"priority\": \"high\"
      }" &
  done < "segments/$segment_name.txt"

  # Rate limiting
  sleep 5
done
```

## 📱 WhatsApp Chat ID Mastery

**🔑 Understanding WhatsApp addressing for maximum reach**

### 📋 Supported Chat ID Formats

| Format | Example | Description | Use Case |
|--------|---------|-------------|----------|
| **Individual** | `923164525711@s.whatsapp.net` | Personal chats | 1:1 communication |
| **Group** | `120363424911005190@g.us` | Group conversations | Community engagement |
| **Broadcast** | `123456789@broadcast` | Broadcast lists | Mass messaging |
| **Business** | `923164525711@c.us` | Business accounts | Customer support |

### 🔄 Automatic Format Normalization

```javascript
// Our API automatically handles format conversion:
"923164525711@c.us" → "923164525711@s.whatsapp.net"
"923164525711" → "923164525711@s.whatsapp.net"
```

### 🎯 Best Practices for Chat ID Management

```bash
# Validate chat IDs before sending
function validate_chat_id() {
  local chat_id="$1"
  if [[ "$chat_id" =~ ^[0-9]+@(s\.whatsapp\.net\|g\.us\|broadcast)$ ]] ||
     [[ "$chat_id" =~ ^[0-9]+$ ]]; then
    return 0 # Valid
  else
    return 1 # Invalid
  fi
}

# Extract phone number from chat ID
function extract_phone() {
  echo "$1" | sed 's/@.*//'
}
```

### 📊 Advanced Chat ID Management

```json
{
  "contacts": {
    "john_doe": {
      "chat_id": "923164525711@s.whatsapp.net",
      "name": "John Doe",
      "tags": ["customer", "premium"],
      "last_contact": "2023-12-25"
    },
    "marketing_group": {
      "chat_id": "120363424911005190@g.us",
      "name": "Exclusive Offers",
      "member_count": 157,
      "engagement_rate": "85%"
    }
  }
}
```

## ⚠️ Enterprise-Grade Error Handling

**🛡️ Robust error management for mission-critical applications**

### 📋 Comprehensive Error Codes

| Error Code | HTTP Status | Description | Solution |
|------------|-------------|-------------|----------|
| `NOT_CONNECTED` | 503 | WhatsApp not connected | Check connection, scan QR code |
| `MISSING_FIELDS` | 400 | Required fields missing | Provide all required parameters |
| `INVALID_CHATID` | 400 | Invalid chat ID format | Use correct WhatsApp ID format |
| `DOWNLOAD_FAILED` | 408 | File download failed | Check URL, network, permissions |
| `FFMPEG_FAILED` | 500 | FFmpeg processing failed | Verify file formats, check logs |
| `FILE_TOO_LARGE` | 413 | File exceeds size limits | Compress file or use document mode |
| `SEND_FAILED` | 500 | Failed to send message | Check WhatsApp status, retry |
| `INTERNAL_ERROR` | 500 | Internal server error | Check server logs, restart |
| `RATE_LIMITED` | 429 | Too many requests | Implement rate limiting |
| `AUTHENTICATION_FAILED` | 401 | Authentication error | Re-authenticate WhatsApp |

### 🔍 Detailed Error Response Structure

```json
{
  "success": false,
  "error": {
    "code": "DOWNLOAD_FAILED",
    "message": "Failed to download video from provided URL",
    "details": {
      "url": "https://example.com/video.mp4",
      "attempts": 3,
      "lastError": "ETIMEDOUT: Connection timeout",
      "timestamp": "2023-12-30T08:32:07.123Z"
    },
    "suggestions": [
      "Check if the URL is accessible",
      "Verify the file exists at the URL",
      "Test with a different video URL",
      "Check your network connection"
    ],
    "documentation": "https://conversoempire.com/docs/error-handling"
  },
  "requestId": "req_abc123def456",
  "timestamp": "2023-12-30T08:32:07.123Z"
}
```

### 🛠️ Error Handling Best Practices

```javascript
// Node.js example with comprehensive error handling
async function sendVideoSafely(videoUrl, chatId) {
  try {
    const response = await axios.post('http://localhost:5000/api/send-video-url', {
      type: 'direct',
      video_url: videoUrl,
      chat_id: chatId
    });

    if (!response.data.success) {
      throw new Error(response.data.error.message);
    }

    return response.data;
  } catch (error) {
    console.error('Video send failed:', error.message);

    // Implement retry logic
    if (error.response?.data?.error?.code === 'NOT_CONNECTED') {
      await reconnectWhatsApp();
      return sendVideoSafely(videoUrl, chatId); // Retry
    }

    // Fallback handling
    if (error.response?.data?.error?.code === 'FILE_TOO_LARGE') {
      return sendAsDocument(videoUrl, chatId);
    }

    // Notification
    sendAlert(`Video send failed: ${error.message}`);

    throw error;
  }
}
```

### 📊 Error Monitoring Dashboard

```json
{
  "errorStats": {
    "totalErrors": 42,
    "errorBreakdown": {
      "NOT_CONNECTED": 12,
      "DOWNLOAD_FAILED": 8,
      "INVALID_CHATID": 6,
      "FILE_TOO_LARGE": 5,
      "SEND_FAILED": 11
    },
    "errorTrends": {
      "last24h": 42,
      "last7d": 189,
      "last30d": 876
    },
    "mostCommonErrors": [
      {
        "code": "SEND_FAILED",
        "count": 11,
        "percentage": 26.19
      },
      {
        "code": "NOT_CONNECTED",
        "count": 12,
        "percentage": 28.57
      }
    ]
  }
}
```

## 🚀 Production Deployment Guide

**🏗️ From development to production - best practices for scaling**

### 📈 Deployment Strategies

| Strategy | Complexity | Scalability | Best For |
|----------|------------|-------------|----------|
| **Single Container** | ⭐ Low | ⭐⭐ Medium | Development, Testing |
| **Docker Compose** | ⭐⭐ Medium | ⭐⭐⭐ High | Production, Small-Medium |
| **Kubernetes** | ⭐⭐⭐⭐ High | ⭐⭐⭐⭐⭐ Very High | Enterprise, Large Scale |
| **Serverless** | ⭐⭐⭐ Medium | ⭐⭐⭐⭐ High | Event-Driven |

### 🐳 Docker Compose Production Setup

```yaml
# docker compose.prod.yml
version: '3.8'

services:
  whatsapp-video-api:
    image: muhammadgohar/whatsapp-ffmpeg-video-api:latest
    container_name: whatsapp-video-api-prod
    restart: always
    ports:
      - "5000:5000"
    volumes:
      - ./auth_data:/app/auth_info_baileys
      - ./video_cache:/tmp/whatsapp-videos
    environment:
      - NODE_ENV=production
      - PORT=5000
      - LOG_LEVEL=warn
      - MAX_CONCURRENT_DOWNLOADS=10
      - DOWNLOAD_TIMEOUT=600000
    healthcheck:
      test: ["CMD", "node", "-e", "require('http').get('http://localhost:5000/api/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"]
      interval: 15s
      timeout: 5s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '2.0'
          memory: 2G
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 30 --cleanup
    restart: unless-stopped

volumes:
  auth_data:
    driver: local
    driver_opts:
      type: none
      device: ./auth_data
      o: bind
  video_cache:
    driver: local
    driver_opts:
      type: none
      device: ./video_cache
      o: bind
```

### 🔧 Deployment Checklist

```markdown
- [ ] ✅ Docker and Docker Compose installed
- [ ] ✅ Port 5000 available on host
- [ ] ✅ Sufficient disk space (10GB+ recommended)
- [ ] ✅ Backup strategy for auth_data volume
- [ ] ✅ Monitoring and alerting configured
- [ ] ✅ Firewall rules updated (if applicable)
- [ ] ✅ SSL/TLS configured for production
- [ ] ✅ Regular backup schedule established
- [ ] ✅ Health monitoring dashboard set up
- [ ] ✅ Auto-update strategy implemented
```

### 📊 Monitoring and Maintenance

```bash
# Comprehensive monitoring script
#!/bin/bash

# Health check
health_status=$(curl -s http://localhost:5000/api/health | jq -r '.status')

# Resource monitoring
cpu_usage=$(docker stats --no-stream --format "{{.CPUPerc}}" whatsapp-video-api-prod | sed 's/%//')
mem_usage=$(docker stats --no-stream --format "{{.MemUsage}}" whatsapp-video-api-prod)

# Alerting
if [ "$health_status" != "connected" ]; then
  echo "CRITICAL: Service not healthy - $health_status" | mail -s "WhatsApp API Alert" ops@conversoempire.com
fi

if [ "$cpu_usage" -gt 90 ]; then
  echo "WARNING: High CPU usage - ${cpu_usage}%" | mail -s "WhatsApp API Warning" ops@conversoempire.com
fi

# Log rotation
docker logs --tail 1000 whatsapp-video-api-prod > api-logs-$(date +%Y%m%d).log
```

### 🔄 Update Strategy

```bash
# Zero-downtime update procedure
#!/bin/bash

# Step 1: Pull latest image
docker compose pull

# Step 2: Create new container
docker compose up -d --no-deps --build whatsapp-video-api

# Step 3: Verify health
for i in {1..10}; do
  if curl -s http://localhost:5000/api/health | jq -e '.status == "connected"' >/dev/null; then
    echo "Update successful!"
    exit 0
  fi
  sleep 5
done

# Step 4: Rollback on failure
echo "Update failed, rolling back..."
docker compose down
docker compose up -d
```

### 🛡️ Security Best Practices

```markdown
1. **Network Security**
   - Use firewall rules to restrict access
   - Consider VPN for remote access
   - Implement rate limiting

2. **Data Security**
   - Encrypt sensitive data at rest
   - Regular backups with encryption
   - Secure volume permissions

3. **Authentication**
   - Add API key authentication
   - Implement IP whitelisting
   - Use HTTPS with valid certificates

4. **Monitoring**
   - Set up intrusion detection
   - Monitor for unusual activity
   - Regular security audits
```

### 📈 Performance Optimization

```json
{
  "performanceTips": [
    {
      "category": "Hardware",
      "tips": [
        "Use SSD storage for better I/O performance",
        "Allocate sufficient RAM (4GB+ recommended)",
        "Consider multi-core CPU for concurrent processing"
      ]
    },
    {
      "category": "Configuration",
      "tips": [
        "Adjust MAX_CONCURRENT_DOWNLOADS based on workload",
        "Optimize timeout values for your network",
        "Use appropriate LOG_LEVEL for production"
      ]
    },
    {
      "category": "Deployment",
      "tips": [
        "Use Docker volumes for persistent data",
        "Implement proper resource limits",
        "Consider container orchestration for scaling"
      ]
    }
  ]
}
```

## 👨‍💻 Developer Guide

**🔧 For contributors and advanced users**

### 🚀 Local Development Setup

```bash
# Step 1: Clone the repository
git clone https://github.com/muhammadgohar/whatsapp-ffmpeg-video-api.git
cd whatsapp-ffmpeg-video-api

# Step 2: Install dependencies
npm install

# Step 3: Configure environment
cp .env.example .env
nano .env  # Edit configuration

# Step 4: Start development server
npm run dev

# Step 5: Access API
curl http://localhost:5000/api/health
```

### 🧪 Testing Framework

```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Test specific endpoint
npm run test:api -- --endpoint send-video-url

# Generate test coverage report
npm run test:coverage
```

### 📦 Project Structure

```
whatsapp-ffmpeg-video-api/
├── src/
│   ├── api/                  # API endpoints
│   ├── services/             # Core services
│   ├── utils/                # Utility functions
│   ├── config/               # Configuration
│   └── models/               # Data models
├── tests/                    # Test suites
├── scripts/                  # Helper scripts
├── .dockerignore             # Docker ignore rules
├── Dockerfile                # Container definition
├── docker compose.yml        # Deployment config
├── package.json              # Dependencies
└── README.md                 # Documentation
```

### 🔨 Development Best Practices

```javascript
// Code style guide
const config = {
  // Use environment variables
  port: process.env.PORT || 5000,

  // Type safety
  maxVideoSize: parseInt(process.env.MAX_VIDEO_SIZE_MB) || 100,

  // Error handling
  validateConfig() {
    if (this.port < 1024 || this.port > 65535) {
      throw new Error('Invalid port number');
    }
  }
};

// Logging best practices
const logger = require('./logger');
logger.info('Starting video processing...');
logger.debug('Video URL:', videoUrl);
logger.warn('High memory usage detected');
logger.error('Failed to send video:', error);
```

### 📚 API Development Tips

```markdown
1. **Endpoint Design**
   - Use RESTful conventions
   - Keep URLs simple and intuitive
   - Version your API (/v1/, /v2/)

2. **Error Handling**
   - Provide meaningful error messages
   - Use appropriate HTTP status codes
   - Include error details for debugging

3. **Performance**
   - Implement caching where possible
   - Optimize database queries
   - Use streaming for large files

4. **Security**
   - Validate all inputs
   - Sanitize user data
   - Implement rate limiting
```

### 🤝 Contributing Guidelines

```markdown
1. **Fork the repository**
2. **Create a feature branch**
   git checkout -b feature/your-feature-name
3. **Commit your changes**
   git commit -m "Add your feature description"
4. **Push to your branch**
   git push origin feature/your-feature-name
5. **Create a Pull Request**

**Code Review Checklist:**
- [ ] Follows project coding standards
- [ ] Includes comprehensive tests
- [ ] Updates documentation
- [ ] Handles edge cases
- [ ] Maintains backward compatibility
```

### 🔬 Debugging Techniques

```bash
# Debug container issues
docker exec -it whatsapp-video-api sh

# View real-time logs
docker logs -f whatsapp-video-api

# Inspect container resources
docker stats whatsapp-video-api

# Debug network issues
docker network inspect bridge

# Profile performance
node --inspect index.js
```

### 📈 Performance Profiling

```javascript
// Performance monitoring
const startTime = process.hrtime();

async function processVideo() {
  // Your video processing logic
}

processVideo().then(() => {
  const [seconds, nanoseconds] = process.hrtime(startTime);
  console.log(`Processing time: ${seconds}s ${nanoseconds/1000000}ms`);
});

// Memory monitoring
setInterval(() => {
  const memoryUsage = process.memoryUsage();
  console.log('Memory usage:', {
    rss: `${(memoryUsage.rss / 1024 / 1024).toFixed(2)} MB`,
    heapTotal: `${(memoryUsage.heapTotal / 1024 / 1024).toFixed(2)} MB`,
    heapUsed: `${(memoryUsage.heapUsed / 1024 / 1024).toFixed(2)} MB`
  });
}, 60000);
```

## 🆘 Comprehensive Troubleshooting Guide

**🔧 Solutions to common issues and advanced debugging**

### 🎬 FFmpeg Issues

**Symptoms:**
- `FFMPEG_FAILED` errors
- Video processing hangs
- Audio merge failures

**Solutions:**

```bash
# Check FFmpeg installation
ffmpeg -version

# Test FFmpeg functionality
ffmpeg -i input.mp4 -c copy output.mp4

# Common fixes:
1. Ensure FFmpeg is in system PATH
2. Check file format compatibility
3. Verify sufficient disk space
4. Update FFmpeg to latest version
```

### 🔌 Connection Problems

**Symptoms:**
- `NOT_CONNECTED` errors
- QR code not generating
- Frequent disconnections

**Diagnostic Steps:**

```bash
# Check WhatsApp connection status
curl http://localhost:5000/api/health | jq '.whatsapp'

# Common solutions:
1. Restart the container: docker restart whatsapp-video-api
2. Clear auth data: rm -rf auth_info_baileys/*
3. Check network connectivity
4. Verify WhatsApp account status
```

### 📦 File Handling Issues

**Symptoms:**
- `DOWNLOAD_FAILED` errors
- File size limit exceeded
- Temporary file cleanup problems

**Troubleshooting:**

```bash
# Check temporary directory
ls -lh /tmp/whatsapp-videos/

# Monitor disk space
df -h

# Solutions:
1. Increase MAX_VIDEO_SIZE_MB for large files
2. Clean up temporary files regularly
3. Verify URL accessibility
4. Check download timeouts
```

### 📊 Performance Optimization

**Symptoms:**
- Slow response times
- High CPU/memory usage
- Queue backlogs

**Optimization Techniques:**

```bash
# Monitor resource usage
docker stats whatsapp-video-api

# Performance tuning:
1. Adjust MAX_CONCURRENT_DOWNLOADS
2. Optimize FFMPEG_TIMEOUT settings
3. Increase system resources
4. Implement load balancing
```

### 🔒 Security Considerations

**Best Practices:**

```markdown
1. **Network Security**
   - Use firewall rules: ufw allow 5000/tcp
   - Implement IP whitelisting
   - Consider VPN for remote access

2. **Data Protection**
   - Encrypt sensitive volumes
   - Regular security audits
   - Monitor for suspicious activity

3. **Authentication**
   - Add API key validation
   - Implement rate limiting
   - Use HTTPS with valid certificates
```

### 📞 Support Resources

```markdown
**Official Support Channels:**
- Email: support@conversoempire.com
- Documentation: https://conversoempire.com/docs
- Community Forum: https://community.conversoempire.com

**Self-Help Resources:**
- Knowledge Base: https://conversoempire.com/kb
- API Reference: https://conversoempire.com/api-docs
- Status Page: https://status.conversoempire.com

**Emergency Contacts:**
- 24/7 Support: +1 (555) 123-4567
- Critical Issues: emergency@conversoempire.com
```

### 🔄 Recovery Procedures

**Disaster Recovery Plan:**

```bash
# Backup procedure
tar -czvf whatsapp-api-backup-$(date +%Y%m%d).tar.gz auth_info_baileys/ video_cache/

# Restore procedure
tar -xzvf whatsapp-api-backup.tar.gz
docker restart whatsapp-video-api

# Emergency rollback
git checkout stable-version
docker compose down && docker compose up -d --build
```

### 📈 Common Error Patterns

| Error Pattern | Likely Cause | Solution |
|---------------|--------------|----------|
| Frequent `NOT_CONNECTED` | Network issues | Check connectivity, restart |
| `DOWNLOAD_FAILED` on specific URLs | URL restrictions | Verify URL accessibility |
| High memory usage | Large file processing | Increase memory limits |
| Slow response times | Resource contention | Optimize configuration |
| `FFMPEG_FAILED` on merge | Format incompatibility | Convert files first |

### 🛠️ Advanced Debugging

```bash
# Container debugging
docker exec -it whatsapp-video-api sh

# Network diagnostics
docker network inspect bridge

# Process monitoring
ps aux | grep node

# Log analysis
docker logs whatsapp-video-api | grep ERROR
```

## 📜 License & Legal

**📋 Open Source License:** MIT License

```markdown
Copyright (c) 2023 Converso Empire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

**🏛️ About Converso Empire**

![Converso Empire Logo](https://via.placeholder.com/200x100/007BFF/FFFFFF?text=Converso+Empire)

**Empire of Innovation, Creativity & Intelligence**

Converso Empire is not just a company - we are a global movement dedicated to building the future of artificial intelligence, design, communication, and digital experiences. Founded by visionary leaders and powered by world-class engineers, we are redefining what's possible in digital technology.

### 🌍 Our Global Mission

> "Building the future, one innovation at a time."

At Converso Empire, we believe in the power of technology to transform lives, businesses, and societies. Our mission is to create intelligent, creative, and powerful products that bridge the gap between human potential and technological capability.

### 🚀 Our Innovative Products

**WhatsApp Video Sender API** - Revolutionizing digital communication with intelligent video delivery

**AI Communication Suite** - Next-generation messaging platforms with artificial intelligence

**Digital Experience Platform** - Creating immersive digital experiences across all channels

**Automation Engine** - Intelligent workflow automation for businesses of all sizes

### 💡 Core Values

```markdown
✅ **Innovation First** - We push boundaries and challenge the status quo
✅ **Quality Obsession** - Excellence in every line of code and every pixel
✅ **Customer Focus** - Solving real problems with real impact
✅ **Collaboration** - Building together, growing together
✅ **Integrity** - Transparency, honesty, and ethical practices
✅ **Continuous Learning** - Always evolving, always improving
```

### 🌟 Why Choose Converso Empire?

```markdown
🔹 **Cutting-Edge Technology** - Built on the latest advancements
🔹 **Enterprise-Grade Reliability** - Designed for mission-critical applications
🔹 **Developer-Friendly** - Intuitive APIs and comprehensive documentation
🔹 **Global Support** - 24/7 assistance from our expert team
🔹 **Innovation Pipeline** - Continuous updates and new features
🔹 **Community Driven** - Powered by a global network of innovators
```

### 🤝 Join the Converso Empire

```markdown
**Careers:** https://conversoempire.com/careers
**Partnerships:** https://conversoempire.com/partners
**Investor Relations:** https://conversoempire.com/investors
**Community:** https://community.conversoempire.com
```

**📞 Contact Us**

```markdown
📧 General Inquiries: info@conversoempire.com
📞 Support Hotline: +1 (555) 123-4567
🌐 Website: https://conversoempire.com
📍 Headquarters: Silicon Valley, California
```

**💬 Social Media**

```markdown
🐦 Twitter: @ConversoEmpire
📘 Facebook: /ConversoEmpire
📸 Instagram: @ConversoEmpire
🔗 LinkedIn: /company/conversoempire
🎥 YouTube: /ConversoEmpire
```

**📢 Stay Updated**

Subscribe to our newsletter for the latest innovations, product updates, and exclusive content from Converso Empire:

```bash
curl https://newsletter.conversoempire.com/subscribe \
  -X POST \
  -d '{"email": "your@email.com", "interests": ["api", "innovation"]}'
```

---

**🏆 A Product of Converso Empire**

This WhatsApp Video Sender API represents the pinnacle of our innovation in digital communication technology. Developed by our world-class engineering team and backed by Converso Empire's commitment to excellence, this product embodies our mission to revolutionize how the world communicates through intelligent, creative, and powerful technology solutions.

> "At Converso Empire, we don't just build software - we build the future."

**© 2023 Converso Empire. All rights reserved.**
