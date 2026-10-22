from datetime import datetime, UTC
from uuid import uuid4
import json


message = {
    "id": str(uuid4()),
    
    #VARS
    
    "created_at": datetime.now(UTC).isoformat()
}

with open ("body.json", "w") as f:
    json.dump(message, f)

