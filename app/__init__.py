from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid

app = FastAPI(
    title="DBM AI Calling Agent",
    version="0.1.0",
    description="Starter backend for telemarketing AI call orchestration",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


class CampaignCreate(BaseModel):
    name: str = Field(..., min_length=2)
    objective: str = Field(..., min_length=5)
    script: str = Field(..., min_length=10)
    target_audience: str = "SMB"
    timezone: str = "UTC"


class LeadCreate(BaseModel):
    name: str
    phone: str
    company: Optional[str] = None
    status: str = "new"
    source: str = "manual"
    priority: str = "normal"


class AgentCreate(BaseModel):
    name: str
    voice: str = "en-US-Neural2-A"
    model: str = "gpt-4o-mini"
    language: str = "en-US"
    region: str = "US"


class CallRequest(BaseModel):
    campaign_id: str
    agent_id: str
    lead_id: str
    call_type: str = "outbound"
    notes: Optional[str] = None


campaigns: Dict[str, Dict[str, Any]] = {}
leads: Dict[str, Dict[str, Any]] = {}
calls: Dict[str, Dict[str, Any]] = {}
agents: Dict[str, Dict[str, Any]] = {}


def generate_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@app.get("/")
def dashboard():
    return JSONResponse({
        "message": "DBM AI Calling Agent is running",
        "docs": "/docs",
        "dashboard": "/static/index.html",
    })


@app.get("/health")
def healthcheck():
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@app.get("/api/campaigns")
def list_campaigns():
    return {"campaigns": list(campaigns.values())}


@app.post("/api/campaigns")
def create_campaign(payload: CampaignCreate):
    campaign_id = generate_id("camp")
    campaign = {
        "id": campaign_id,
        "name": payload.name,
        "objective": payload.objective,
        "script": payload.script,
        "target_audience": payload.target_audience,
        "timezone": payload.timezone,
        "created_at": datetime.utcnow().isoformat(),
    }
    campaigns[campaign_id] = campaign
    return {"message": "Campaign created", "campaign": campaign}


@app.get("/api/leads")
def list_leads():
    return {"leads": list(leads.values())}


@app.post("/api/leads")
def create_lead(payload: LeadCreate):
    lead_id = generate_id("lead")
    lead = {
        "id": lead_id,
        "name": payload.name,
        "phone": payload.phone,
        "company": payload.company,
        "status": payload.status,
        "source": payload.source,
        "priority": payload.priority,
        "created_at": datetime.utcnow().isoformat(),
    }
    leads[lead_id] = lead
    return {"message": "Lead created", "lead": lead}


@app.get("/api/agents")
def list_agents():
    if not agents:
        default_agent = {
            "id": "agent_default",
            "name": "Sales Caller Agent",
            "voice": "en-US-Neural2-A",
            "model": "gpt-4o-mini",
            "language": "en-US",
            "region": "US",
        }
        agents[default_agent["id"]] = default_agent
    return {"agents": list(agents.values())}


@app.post("/api/agents")
def create_agent(payload: AgentCreate):
    agent_id = generate_id("agent")
    agent = {
        "id": agent_id,
        "name": payload.name,
        "voice": payload.voice,
        "model": payload.model,
        "language": payload.language,
        "region": payload.region,
        "created_at": datetime.utcnow().isoformat(),
    }
    agents[agent_id] = agent
    return {"message": "Agent created", "agent": agent}


@app.get("/api/calls")
def list_calls():
    return {"calls": list(calls.values())}


@app.post("/api/agents/{agent_id}/call")
def create_call(agent_id: str, payload: CallRequest):
    if agent_id != payload.agent_id:
        return JSONResponse(status_code=400, content={"message": "Agent ID mismatch"})

    call_id = generate_id("call")
    call = {
        "id": call_id,
        "campaign_id": payload.campaign_id,
        "agent_id": agent_id,
        "lead_id": payload.lead_id,
        "call_type": payload.call_type,
        "status": "queued",
        "notes": payload.notes or "",
        "created_at": datetime.utcnow().isoformat(),
        "summary": "Call queued for orchestration.",
    }
    calls[call_id] = call
    return {"message": "Call placed", "call": call}


@app.get("/api/health")
def api_health():
    return {
        "status": "ready",
        "campaigns": len(campaigns),
        "leads": len(leads),
        "calls": len(calls),
        "agents": len(agents),
    }


@app.post("/api/calls/{call_id}/status")
def update_call_status(call_id: str, payload: Dict[str, Any]):
    if call_id not in calls:
        return JSONResponse(status_code=404, content={"message": "Call not found"})

    status = payload.get("status", "queued")
    summary = payload.get("summary", calls[call_id].get("summary"))
    calls[call_id]["status"] = status
    calls[call_id]["summary"] = summary
    calls[call_id]["updated_at"] = datetime.utcnow().isoformat()
    return {"message": "Call status updated", "call": calls[call_id]}

