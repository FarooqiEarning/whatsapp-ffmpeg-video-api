# Use official Node.js LTS image
FROM node:18-alpine

# Install FFmpeg and other dependencies
RUN apk add --no-cache ffmpeg

# Create app directory
WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Create temp directory
RUN mkdir -p /tmp/whatsapp-videos

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["node", "index.js"]
