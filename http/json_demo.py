import json
from datetime import UTC, datetime
from uuid import uuid4

var_example = 100

message = {
    "id": str(uuid4()), 
    #A UUID is a random ID that is effectively guaranteed to be unique. 
    # You don’t need a central counter or a database to hand out numbers, so any client can create IDs on its own without clashing with anyone else.
    
    "text": "Hello",
    "final": var_example,
    
    "speaker": False,
    
    "created_at": datetime.now(UTC).isoformat(),
    }

body = json.dumps(message) #py dict to json text

print(body)

back = json.loads(body) #json text to py dict

print(back["final"] is True,
back["speaker"] is None)




body_dictionary_message = {
    "id": str(uuid4()),
    
    #Any other data you want in here
    
    "created_at": datetime.now(UTC).isoformat(),   
}
    


body_for_json = {
    "id": str(uuid4()),
    
    
    "created_at": datetime.now(UTC).isoformat(),
}



new_body_2 = {
    "id": str(uuid4()),
    "created_at": datetime.now(UTC).isoformat(),
}



"""

curl.exe -i -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d "@body.json"


curl.exe -i https://httpbin.org/get

curl.exe -i -X POST https://httpbin.org/post -H "Content-Type: application/json" -d "@body.json"
curl.exe -i -X PUT https://httpbin.org/put -H "Content-Type: application/json" -d "@body.json"
curl.exe -i -X DELETE https://httpbin.org/delete


curl.exe	The real curl, not PowerShell’s alias
-i	Show the response status and headers
-X POST	The method
URL	Where to send it
-H "..."	The header saying the body is JSON
-d "@body.json"	The body, read from the file. The @ means “from this file”

"""