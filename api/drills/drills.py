"""Pydantic drills. Fill in every TODO and fix the broken bits.

Run from the api\drills folder:
    uv run --with pytest python -m pytest -q
"""

from datetime import UTC, datetime
from typing import Literal, Self
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    # TODO 1: id must be a UUID made automatically for each message (Field(default_factory=...)).
    id: UUID

    # TODO 2: role must be exactly "user", "assistant" or "system".
    role: str

    text: str = Field(min_length=1, max_length=4000)
    audio_ms: int | None = Field(default=None, ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # BROKEN: this check never returns the value. Fix it.
    @field_validator("text")
    @classmethod
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")


class Transcript(BaseModel):
    text: str

    # TODO 3: language must be exactly "en-GB" or "en-US".
    language: str

    confidence: float = Field(ge=0, le=1)
    duration_ms: int = Field(ge=0)
    start_ms: int = Field(ge=0)
    end_ms: int = Field(ge=0)

    # TODO 4: reject the transcript when end_ms is not greater than start_ms.
    # Use @model_validator(mode="after"), take self, and return self.


def make_message(**kwargs) -> Message:
    # TODO 5: build and return a Message from the keyword arguments.
    raise NotImplementedError


def error_locations(data: dict) -> list[tuple]:
    # TODO 6: try to build a Message from data.
    # If ValidationError is raised, return the "loc" of each error.
    # If it works, return an empty list.
    raise NotImplementedError


def round_trip(message: Message) -> Message:
    # TODO 7: turn the message into JSON text, then read that text back into a Message and return it.
    raise NotImplementedError
