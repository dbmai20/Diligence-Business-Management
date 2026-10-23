# Diligence Business Management

AI-powered telemarketing calling agent for outbound lead qualification, call routing, and CRM tracking.

## Overview

This starter project includes:
- FastAPI backend for campaign and call orchestration
- Simple browser dashboard for monitoring calls and campaigns
- In-memory persistence for local development
- Ready-to-extend structure for Twilio, Telephony, CRM, and lead scoring integrations

## Architecture

- `app/main.py` — FastAPI application and API endpoints
- `app/static/` — lightweight dashboard UI
- `requirements.txt` — Python dependencies

## Features

- Create campaigns
- Add leads and call goals
- Trigger AI call sessions
- Monitor call status
- View transcript summaries and activity logs
- Extend with telephony providers and LLM-based voice orchestration

## Quick start

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. Open the dashboard:
   - API docs: http://localhost:8000/docs
   - Dashboard: http://localhost:8000/

## Key API routes

- `GET /health`
- `GET /api/campaigns`
- `POST /api/campaigns`
- `GET /api/leads`
- `POST /api/leads`
- `GET /api/agents`
- `POST /api/agents/{agent_id}/call`
- `GET /api/calls`

## Suggested next steps

- Connect to Twilio Voice or another telephony provider
- Add real LLM orchestration for call handling
- Persist CRM and call metadata in PostgreSQL or SQLite
- Add outbound dialer logic with scheduling and lead scoring

## Notes

This repository is intentionally scaffolded as a strong starting point for a production-ready telemarketing AI agent. The current implementation uses in-memory state so it can run immediately without setup complexity.
