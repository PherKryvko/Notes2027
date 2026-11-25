"""Reference solutions. Open only after you have tried each drill."""
from datetime import UTC, datetime
from typing import Literal, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Literal["user", "assistant"]
    text: str = Field(min_length=1)
    audio_ms: int | None = None


class Note(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")
        return value  # the fix: whatever you return becomes the field's value


class Transcript(BaseModel):
    start_ms: int
    end_ms: int

    @model_validator(mode="after")
    def end_after_start(self) -> Self:
        if self.end_ms <= self.start_ms:
            raise ValueError("end_ms must be greater than start_ms")
        return self


class Event(BaseModel):
    name: str
    id: UUID = Field(default_factory=uuid4)  # called once per object
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    seen_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


def to_wire(item: Item) -> dict:
    return item.model_dump(mode="json")


def from_wire(raw: str) -> Item:
    return Item.model_validate_json(raw)
