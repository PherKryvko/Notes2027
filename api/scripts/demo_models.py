from pydantic import ValidationError       # the error Pydantic raises when data is wrong
from app.models import Message, Conversation, Transcript # the models we just wrote
from time import sleep                     # only for pausing, not needed for the models

# Build a Message from a dict (like data from a request). "1840" is converted to the number 1840.
m = Message.model_validate({"role": "user", "text": "Hello", "audio_ms": "1840"})

# Turn the model into a dict for printing. Leave out id and created_at so the output is short.
print(m.model_dump(mode="json", exclude={"id", "created_at"}))

sleep(1)  # not needed here. It only slowed the script down, so you can remove it.

# Bad data: "robot" is not allowed and "" is too short. Catch the error and print each problem.
try:
    Message.model_validate({"role": "robot", "text": ""})
except ValidationError as exc:
    for err in exc.errors():
        print(err["loc"], err["type"])  # loc says which field, type says what went wrong
        
    
try: 
    Transcript.model_validate({"text": "Hello Sir", "language": "en-US", "confidence" : "1", "duration_ms": 1})
except ValidationError as exc:
    for err in exc.errors():
        print("Transcript", err["loc"], err["type"])
        
    
    