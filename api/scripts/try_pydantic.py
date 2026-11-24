# api/scripts/try_pydantic.py
from pydantic import BaseModel, ValidationError


class M(BaseModel): #Pydantic's base class : inheritted for validation
    role: str
    text: str
    
m =M(role="user", text="Hello")

print(m)
print(m.text)
        