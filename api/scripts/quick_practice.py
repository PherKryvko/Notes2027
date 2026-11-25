"""Quick Pydantic practice. Fill in each TODO, closed-book, then run the file.

Run from the api/scripts folder:
    uv run --with pydantic python quick_practice.py

Each section prints a line. The "expect" comment shows what the line should look like.
Work one section at a time. Run after each one.
"""

from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator


# 1. TODO: class Person with name (str) and age (int).
#    Make Person(name="Ana", age="30"). Print 1, the age, and its type.
#    expect: 1 30 <class 'int'>
class Person(BaseModel):
    name: str = Field()
    age: int = Field(ge=0)    
    
p = Person(name="Ana", age="30")
print(f"1 {p.age} {type(p.age)}")


# 2. TODO: make Person(name="Ana", age="thirty") inside try/except ValidationError.
#    In the except, print 2, the "loc" of the first error, and its "type".
#    expect: 2 ('age',) int_parsing

try:
    Person(name="Ana", age="thirty")
except ValidationError as exc:
    print(2, exc.errors()[0]["loc"], exc.errors()[0]["type"])


# 3. TODO: class Note with text (str) and pinned (bool, default False).
#    Make Note(text="hi") and print 3 and its pinned value.
#    expect: 3 False
class Note(BaseModel):
    text: str
    pinned: bool = Field(default=False)
    
note = Note(text="hi")
print(3, note.pinned)
    


# 4. TODO: class Tag with label (str), min_length=2, max_length=10.
#    Make Tag(label="a") inside try/except. Print 4 and the first error's "msg".
#    expect: 4 String should have at least 2 characters
class Tag(BaseModel):
    label: str = Field(min_length=2, max_length=10)
    
try:
    tag = Tag(label="a")
except ValidationError as exc:
    print(4, exc.errors()[0]["msg"])


# 5. TODO: class Strict with model_config = ConfigDict(extra="forbid") and x (int).
#    Make Strict(x=1, y=2) inside try/except. Print 5 and the first error's "type".
#    expect: 5 extra_forbidden
class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")
    x: int = Field(default=0)
    
try:
    s = Strict(x=1, y=10)
except ValidationError as ve:
    print(5, ve.errors()[0]["type"])    

# 6. TODO: use the Person from section 1. Print 6 and its model_dump() dict.
#    Then print 6 and its model_dump_json() text.
#    expect: 6 {'name': 'Ana', 'age': 30}
#            6 {"name":"Ana","age":30}
p = Person(name="Ana", age="10")
print(6, p.model_dump())
print(6, p.model_dump_json())

# 7. TODO: class Name with first (str). Add a field_validator on "first"
#    that strips spaces and returns the value. Print 7 and repr of Name(first="  Ana  ").first.
#    expect: 7 'Ana'


# 8. TODO: class Span with start (int) and end (int). Add a model_validator(mode="after")
#    that raises ValueError("end must be after start") if end <= start. It must return self.
#    Make Span(start=5, end=2) inside try/except. Print 8 and the first error's "msg".
#    expect: 8 Value error, end must be after start


# 9. TODO: class Token with id (str), default_factory=lambda: str(uuid4()).
#    Make two Tokens. Print 9 and whether their ids are different.
#    expect: 9 True


# 10. TODO: class Chat with messages: list of Note, default empty (Field(default_factory=list)).
#     Make Chat(messages=[{"text": "hi"}, {"text": "yo", "pinned": True}]).
#     Print 10, the length of messages, and messages[1].pinned.
#     expect: 10 2 True


# 11. TODO: class Msg with role: Literal["user", "assistant"].
#     Make Msg(role="robot") inside try/except. Print 11 and the first error's "type".
#     expect: 11 literal_error


# 12. TODO: print 12 and Note.model_validate({"text": "from dict"}).text.
#     Then print 12 and Note.model_validate_json('{"text": "from json", "pinned": true}').pinned.
#     expect: 12 from dict
#             12 True
