"""Pydantic drills. Work through the parts in order: each part depends on the ones before it.

Run from the api\drills folder:
    uv run --with pytest python -m pytest -q
"""

from datetime import UTC, datetime
from typing import Literal, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


# ---------------------------------------------------------------------------
# PART 1: Message (the model everything else uses)
# ---------------------------------------------------------------------------
class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # TODO 1: id must be a UUID made automatically for each message (Field(default_factory=...)).
    id: UUID = Field(default_factory=uuid4)

    # TODO 2: role must be exactly "user", "assistant" or "system".
    role: Literal["user", "assistant", "system"]

    text: str = Field(min_length=1, max_length=4000)
    audio_ms: int | None = Field(default=None, ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Fixed: this check now returns the value.
    @field_validator("text")
    @classmethod
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")
        return value


# ---------------------------------------------------------------------------
# PART 2: make a Message from keyword arguments (needs Part 1)
# ---------------------------------------------------------------------------
def make_message(**kwargs) -> Message:
    # TODO 3: build and return a Message from the keyword arguments.
    return Message(**kwargs)
        
    raise NotImplementedError


# ---------------------------------------------------------------------------
# PART 3: read a Message from data and report errors, and round-trip JSON (both need Part 1)
# ---------------------------------------------------------------------------
def error_locations(data: dict) -> list[tuple]:
    # TODO 4: try to build a Message from data.
    # If ValidationError is raised, return the "loc" of each error.
    # If it works, return an empty list.
    
    try:
        Message.model_validate(data)
    except ValidationError as exc:
       return [err["loc"] for err in exc.errors()]
    return []


def round_trip(message: Message) -> Message:
    # TODO 5: turn the message into JSON text, then read that text back into a Message and return it.
    json_text = message.model_dump_json()
    new_message = message.model_validate_json(json_text)
    return new_message

# ---------------------------------------------------------------------------
# PART 4: Transcript (independent of Parts 1 to 3, so it can be done any time)
# ---------------------------------------------------------------------------
class Transcript(BaseModel):
    text: str

    # TODO 6: language must be exactly "en-GB" or "en-US".
    language: Literal["en-GB", "en-US"]

    confidence: float = Field(ge=0, le=1)
    duration_ms: int = Field(ge=0)
    start_ms: int = Field(ge=0)
    end_ms: int = Field(ge=0)
    
    @model_validator(mode="after")
    def ms_greater_start(self) -> Self:
        if self.start_ms > self.end_ms:
            raise ValueError("Start > end, not allowed")
        return self
    
    # TODO 7: reject the transcript when end_ms is not greater than start_ms.
    # Use @model_validator(mode="after"), take self, and return self.
