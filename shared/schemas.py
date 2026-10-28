from pydantic import BaseModel, Field


class TraceEvent(BaseModel):
    """Simple reusable schema for logging structured tool or model events."""
    timestamp: str
    event_type: str
    details: dict = Field(default_factory=dict)


class PromptRequest(BaseModel):
    prompt: str
    model: str = "claude-sonnet-4"
    temperature: float = 0.0
