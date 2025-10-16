from pydantic import BaseModel
 
#define the shape of data your API sends/recieve
class ChatRequest (BaseModel):
    message:str

class ChatResponse(BaseModel):
    reply:str