from fastapi import FastAPI, UploadFile, WebSocket
from queue import Queue
from utils.utilities import PrintInfo
from pydantic import BaseModel

class FileInfo(BaseModel):
    no_of_copies: int
    is_double_side: bool
    page_count: int

app = FastAPI()

SECRET :str = "q$sc6gy^jm0"

file_queue :Queue = Queue(25)

async def sendFile():
    file_name = "tempName"
    return {"filename": file_name}

@app.post("/uploadfile/")
async def queue_file(file: UploadFile, info: FileInfo):
    # print(file.filename, file.content_type,"hhhh")
    print_info = PrintInfo(file, info.no_of_copies, info.is_double_side, info.page_count)
    file_queue.put(print_info)
    return {"info" : {
        "status" : "queued",
        "cost" : print_info.calculate_cost()
    }}

@app.websocket("/ws/{info: str}")
async def root(websocket: WebSocket, info: str):
    if(info != SECRET):
        return "Permission denied"
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        fileinfo: UploadFile = file_queue.get().file
        await websocket.send_text(str(fileinfo.size))
        await websocket.send_bytes(fileinfo.file.read())
        # await websocket.send_text(file_queue.get())
        data = await websocket.receive_text()
