#!/bin/bash

# Portfolio Frontend Startup Script

echo "🎨 Starting Portfolio Frontend..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Check if .env.local exists
if [ ! -f ".env.local" ]; then
    echo "⚠️  No .env.local found, creating from example..."
    cp .env.local.example .env.local
    echo "✅ Created .env.local (using default: http://localhost:8000)"
fi

# Start development server
echo "✨ Starting Next.js development server..."
npm run dev