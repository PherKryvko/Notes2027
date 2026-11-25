"""Tests for the Pydantic drills.

Runs drills.py by default. To check the model answers instead:
    $env:DRILLS_MODULE = "solutions"
"""

import importlib
import os
from uuid import uuid4

import pytest
from pydantic import ValidationError

mod = importlib.import_module(os.environ.get("DRILLS_MODULE", "drills"))
Message = mod.Message
Transcript = mod.Transcript
make_message = mod.make_message
error_locations = mod.error_locations
round_trip = mod.round_trip


def good_transcript(**changes):
    data = dict(text="hi", language="en-GB", confidence=0.9, duration_ms=500, start_ms=0, end_ms=500)
    data.update(changes)
    return data


def test_each_message_gets_its_own_id():
    a = make_message(role="user", text="a")
    b = make_message(role="user", text="b")
    assert a.id != b.id, "each Message should get a new id automatically"


def test_role_only_allows_the_three_values():
    assert make_message(role="assistant", text="hi").role == "assistant"
    with pytest.raises(ValidationError):
        make_message(role="robot", text="hi")


def test_text_with_null_byte_is_rejected():
    with pytest.raises(ValidationError):
        make_message(role="user", text="bad\x00text")


def test_normal_text_is_kept_by_the_validator():
    assert make_message(role="user", text="hello").text == "hello"


def test_language_only_allows_en_gb_and_en_us():
    assert Transcript(**good_transcript(language="en-US")).language == "en-US"
    with pytest.raises(ValidationError):
        Transcript(**good_transcript(language="fr-FR"))


def test_transcript_end_must_be_after_start():
    assert Transcript(**good_transcript()).end_ms == 500
    with pytest.raises(ValidationError):
        Transcript(**good_transcript(start_ms=500, end_ms=100))


def test_error_locations_names_the_bad_fields():
    assert error_locations({"id": str(uuid4()), "role": "user", "text": "hi"}) == []
    locs = error_locations({"id": str(uuid4()), "role": "robot", "text": ""})
    assert ("role",) in locs
    assert ("text",) in locs


def test_json_round_trip_gives_the_same_message():
    m = make_message(role="user", text="hello", audio_ms=1840)
    assert round_trip(m) == m
