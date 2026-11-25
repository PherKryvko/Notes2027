"""Pydantic drills. Edit this file, then run the tests (see the 03b note).

Work top to bottom. Each drill has a TODO. Do not open solutions.py until you have tried.
"""
from datetime import UTC, datetime
from typing import Literal, Self
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


# ---------------------------------------------------------------------------
# Drill 1: write a model from scratch
# Message: role is "user" or "assistant" (nothing else), text is at least 1
# character, audio_ms is an optional int that defaults to None.
# Unknown keys must be rejected.
# ---------------------------------------------------------------------------
class Message(BaseModel):
    pass  # TODO


# ---------------------------------------------------------------------------
# Drill 2: fix the bug
# Valid text should come back unchanged. Right now it does not.
# ---------------------------------------------------------------------------
class Note(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:
            raise ValueError("text must not contain null bytes")


# ---------------------------------------------------------------------------
# Drill 3: a rule across two fields
# Reject a Transcript where end_ms is not greater than start_ms.
# ---------------------------------------------------------------------------
class Transcript(BaseModel):
    start_ms: int
    end_ms: int
    # TODO


# ---------------------------------------------------------------------------
# Drill 4: fix the bug
# Every Event should get its OWN id and created_at when it is created.
# Right now every Event shares the same values. Fix it without changing the
# field names or types.
# ---------------------------------------------------------------------------
class Event(BaseModel):
    name: str
    id: UUID = uuid4()
    created_at: datetime = datetime.now(UTC)


# ---------------------------------------------------------------------------
# Drill 5: out to data and back in
# Item is given. Implement the two functions.
#   to_wire(item)  -> dict that json.dumps() accepts (UUID and datetime as text)
#   from_wire(raw) -> Item, parsed and validated from a JSON string
# ---------------------------------------------------------------------------
class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    seen_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


def to_wire(item: Item) -> dict:
    raise NotImplementedError  # TODO


def from_wire(raw: str) -> Item:
    raise NotImplementedError  # TODO
