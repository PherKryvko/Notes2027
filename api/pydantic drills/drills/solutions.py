"""Model answers for the Pydantic drills. Try drills.py first."""

from datetime import UTC, datetime
from typing import Literal, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID = Field(default_factory=uuid4)
    role: Literal["user", "assistant", "system"]
    text: str = Field(min_length=1, max_length=4000)
    audio_ms: int | None = Field(default=None, ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("text")
    @classmethod
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")
        return value


class Transcript(BaseModel):
    text: str
    language: Literal["en-GB", "en-US"]
    confidence: float = Field(ge=0, le=1)
    duration_ms: int = Field(ge=0)
    start_ms: int = Field(ge=0)
    end_ms: int = Field(ge=0)

    @model_validator(mode="after")
    def end_after_start(self) -> Self:
        if self.end_ms <= self.start_ms:
            raise ValueError("end_ms must be greater than start_ms")
        return self


def make_message(**kwargs) -> Message:
    return Message(**kwargs)


def error_locations(data: dict) -> list[tuple]:
    try:
        Message.model_validate(data)
    except ValidationError as exc:
        return [err["loc"] for err in exc.errors()]
    return []


def round_trip(message: Message) -> Message:
    return Message.model_validate_json(message.model_dump_json())
