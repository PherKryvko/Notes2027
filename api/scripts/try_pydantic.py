# api/scripts/try_pydantic.py
from pydantic import BaseModel, ValidationError


class M(BaseModel): #Pydantic's base class : inheritted for validation
    role: str
    text: str
    
m =M(role="user", text="Hello")

print(m)
print(m.text)
        
try:
    M(role="user")
except ValidationError as exc:
    print(exc)
    print(exc.errors()[0]["loc"], exc.errors()[0]["type"])
    
try:
    M(role="user", text=123)
except ValidationError as exc:
    print(exc.errors()[0]["type"])


class M2(BaseModel):
    text: str
    audio_ms: int | None = None
    
m2 = M2(text="a", audio_ms="1840")
print(repr(m2.audio_ms))