from datetime import UTC, datetime      # datetime: a date and time. UTC: the time zone we store in
from typing import Literal, Self        # Literal: a fixed list of allowed values. Self: "this same class" (used as a return type)
from uuid import UUID, uuid4            # UUID: the type for a unique id. uuid4: makes a random one

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
# BaseModel: the parent class that makes a class a validated model
# ConfigDict: settings for the whole model
# Field: attaches rules and defaults to one field
# field_validator / model_validator: let you write your own checks


class Message(BaseModel):
    # Settings for this model: reject any key that isn't a field (catches typos like "txet")
    model_config = ConfigDict(extra="forbid")

    # Unique id. Not passed in by the caller: a new random UUID is made for each message.
    # No brackets on uuid4, because we pass the function, we don't call it here.
    id: UUID = Field(default_factory=uuid4)

    # Only these three values are allowed. "robot" or "toycar" is rejected.
    role: Literal["user", "assistant", "system"]

    # Must be between 1 and 4000 characters, so empty text and huge text are rejected.
    text: str = Field(min_length=1, max_length=4000)

    # Optional number. None if not given. If given, must be 0 or more (ge = greater than or equal).
    audio_ms: int | None = Field(default=None, ge=0)

    # Time the message was made. The lambda runs each time a message is created, not once when the file loads.
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    # Your own rule for the text field. Runs after the normal checks.
    @field_validator("text")
    @classmethod   # makes the first argument the class (cls), not one object (self)
    def no_null_bytes(cls, value: str) -> str:
        if "\x00" in value:          # \x00 is an invisible null character that can break databases
            raise ValueError("text must not contain null bytes")  # this becomes the error message
        return value                 # whatever is returned is the field's stored value. Forgetting this sets it to None.


class Conversation(BaseModel):
    id: UUID = Field(default_factory=uuid4)                # unique id, made automatically
    title: str = Field(default="Untitled", max_length=200) # optional title with a default
    messages: list[Message] = Field(default_factory=list)  # a list of Message objects. A new empty list for each conversation.

    # Runs after all fields are valid, so it can look at several fields together.
    @model_validator(mode="after")
    def must_not_start_with_assistant(self) -> Self:  # self is the conversation being checked
        if self.messages and self.messages[0].role == "assistant":  # if there are messages and the first is from the assistant
            raise ValueError("a conversation cannot start with an assistant message")
        return self  # hand the checked conversation back


class Transcript(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    text: str = Field(max_length=200)
    language: Literal["en-GB", "en-US"]
    confidence: float = Field(ge=0, le=1)
    duration_ms: int = Field(ge=0)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    
