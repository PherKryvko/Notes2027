"""Quick Pydantic experiments. Each numbered section does one thing.

Run from the api/scripts folder:
    uv run --with pydantic python quick_tests.py
"""

from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


# 1. Types are checked. "30" is converted to the int 30.
class Person(BaseModel):
    name: str
    age: int


p = Person(name="Ana", age="30")
print(1, p.age, type(p.age))  # 1 30 <class 'int'>


# 2. Data that cannot be converted is rejected with a ValidationError.
try:
    Person(name="Ana", age="thirty")
except ValidationError as e:
    print(2, e.errors()[0]["loc"], e.errors()[0]["type"])  # 2 ('age',) int_parsing


# 3. A field with a default is optional.
class Note(BaseModel):
    text: str
    pinned: bool = False


print(3, Note(text="hi").pinned)  # 3 False


# 4. Constraints: this text must be 2 to 10 characters.
class Tag(BaseModel):
    label: str = Field(min_length=2, max_length=10)


try:
    Tag(label="a")
except ValidationError as e:
    print(4, e.errors()[0]["msg"])  # 4 String should have at least 2 characters


# 5. extra="forbid" rejects keys the model does not know about.
class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")
    x: int


try:
    Strict(x=1, y=2)
except ValidationError as e:
    print(5, e.errors()[0]["type"])  # 5 extra_forbidden


# 6. Turn the model back into plain data: a dict, then JSON text.
print(6, p.model_dump())       # 6 {'name': 'Ana', 'age': 30}
print(6, p.model_dump_json())  # 6 {"name":"Ana","age":30}


# 7. A field validator checks one field. It must return the value.
class Name(BaseModel):
    first: str

    @field_validator("first")
    @classmethod
    def strip_spaces(cls, value: str) -> str:
        return value.strip()


print(7, repr(Name(first="  Ana  ").first))  # 7 'Ana'


# 8. A model validator sees all fields, so it can compare them. It must return self.
class Span(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def end_after_start(self):
        if self.end <= self.start:
            raise ValueError("end must be after start")
        return self


try:
    Span(start=5, end=2)
except ValidationError as e:
    print(8, e.errors()[0]["msg"])  # 8 Value error, end must be after start


# 9. default_factory runs once for each object, so each id is different.
class Token(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))


a, b = Token(), Token()
print(9, a.id != b.id)  # 9 True


# 10. A list of models: every item is validated as a Note.
class Chat(BaseModel):
    messages: list[Note] = Field(default_factory=list)


c = Chat(messages=[{"text": "hi"}, {"text": "yo", "pinned": True}])
print(10, len(c.messages), c.messages[1].pinned)  # 10 2 True


# 11. Literal: only the listed values are allowed.
class Msg(BaseModel):
    role: Literal["user", "assistant"]


try:
    Msg(role="robot")
except ValidationError as e:
    print(11, e.errors()[0]["type"])  # 11 literal_error


# 12. Build a model from a dict, or from JSON text.
print(12, Note.model_validate({"text": "from dict"}).text)  # 12 from dict
print(12, Note.model_validate_json('{"text": "from json", "pinned": true}').pinned)  # 12 True
