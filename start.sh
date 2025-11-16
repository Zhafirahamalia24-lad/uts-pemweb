#!/bin/bash
set -e
echo "Starting UTS PEMWEB (dev) ..."
# Start backend (non-docker) in background (optional)
if [ -d "backend" ]; then
  (cd backend && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000) &
fi
# Start frontend
if [ -d "frontend" ]; then
  (cd frontend && npm install && npm run dev) &
fi
wait
