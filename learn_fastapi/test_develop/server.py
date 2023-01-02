from fastapi import FastAPI, UploadFile

app = FastAPI()

async def sendFile():
    file_name = "tempName"
    return {"filename": file_name}

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    print(file.filename, file.content_type,"hhhh")
    return {"filename": file.filename}
