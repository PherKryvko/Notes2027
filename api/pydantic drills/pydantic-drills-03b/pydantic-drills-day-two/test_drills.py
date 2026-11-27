import json
import time
from datetime import datetime
from uuid import UUID

import pytest
from pydantic import ValidationError

from drills import Event, Item, Message, Note, Transcript, from_wire, to_wire


# Drill 1 ---------------------------------------------------------------
def test_message_valid_defaults_audio_ms_to_none():
    m = Message(role="user", text="hi")
    assert m.audio_ms is None


def test_message_converts_numeric_string():
    assert Message(role="assistant", text="hi", audio_ms="1840").audio_ms == 1840


def test_message_rejects_bad_role():
    with pytest.raises(ValidationError):
        Message(role="robot", text="hi")


def test_message_rejects_empty_text():
    with pytest.raises(ValidationError):
        Message(role="user", text="")


def test_message_rejects_unknown_key():
    with pytest.raises(ValidationError):
        Message(role="user", text="hi", colour="blue")


def test_message_role_is_exactly_user_or_assistant():
    with pytest.raises(ValidationError):
        Message(role="system", text="hi")


# Drill 2 ---------------------------------------------------------------
def test_note_valid_text_comes_back_unchanged():
    assert Note(text="hello").text == "hello"


def test_note_rejects_null_byte():
    with pytest.raises(ValidationError):
        Note(text="bad\x00text")


# Drill 3 ---------------------------------------------------------------
def test_transcript_accepts_end_after_start():
    t = Transcript(start_ms=0, end_ms=10)
    assert t.end_ms == 10


@pytest.mark.parametrize("start,end", [(10, 10), (10, 5)])
def test_transcript_rejects_end_not_after_start(start, end):
    with pytest.raises(ValidationError):
        Transcript(start_ms=start, end_ms=end)


# Drill 4 ---------------------------------------------------------------
def test_event_ids_differ_per_object():
    assert Event(name="a").id != Event(name="b").id


def test_event_created_at_is_per_object():
    first = Event(name="a")
    time.sleep(0.01)
    second = Event(name="b")
    assert first.created_at < second.created_at


def test_event_keeps_field_types():
    e = Event(name="a")
    assert isinstance(e.id, UUID) and isinstance(e.created_at, datetime)


# Drill 5 ---------------------------------------------------------------
def test_to_wire_is_json_safe():
    wire = to_wire(Item(name="x"))
    json.dumps(wire)  # raises TypeError if a UUID or datetime is left in
    assert isinstance(wire["id"], str) and isinstance(wire["seen_at"], str)


def test_from_wire_round_trip():
    original = Item(name="x")
    back = from_wire(json.dumps(to_wire(original)))
    assert back == original
    assert isinstance(back.seen_at, datetime)


def test_from_wire_rejects_bad_data():
    with pytest.raises(ValidationError):
        from_wire('{"name": 123}')
