# === Stage 1: Build / Install Dependencies ===
FROM node:24.12.0-bookworm AS builder

# metadata
LABEL maintainer="mg03164525711@gmail.com"

# Set workdir
WORKDIR /app

# Install system utilities + FFmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    python3 \
    build-essential \
    libcairo2-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libgif-dev \
    librsvg2-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy just package files for caching
COPY package*.json ./

# Install dependencies via npm ci for reproducible production deps
RUN npm ci --only=production

# Copy the rest of the app
COPY . .

# === Stage 2: Production Image ===
FROM node:24.12.0-bookworm-slim

# non-root appuser for better security
RUN useradd -m appuser
USER appuser

WORKDIR /home/appuser/app

# Copy installed deps and app from builder stage
COPY --from=builder /app /home/appuser/app

# Set environment
ENV NODE_ENV=production
ENV PORT=5000

# Expose app port
EXPOSE 5000

# Healthcheck (calls app’s /api/health endpoint)
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD node -e "require('http').get('http://localhost:5000/api/health', (r) => {process.exit(r.statusCode === 200 ? 0 : 1)})"

# Default start command
CMD ["node", "index.js"]