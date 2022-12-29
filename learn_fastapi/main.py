from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#path parameters with type checking
@app.get("/hello/{name}")
async def hello(name: str):
    return {"message" : f"hello {name}"}

@app.get("/userid/{id}")
async def userid(id: int):
    return {"userid" : id}

#order matters
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#Predefined values for path parameters using enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#Path parameters containing paths
@app.get("/file/{file_path:path}")
async def userpath(file_path: str): #path = /file/aaa/bbb/ccc
    return {"file_path" : file_path} #returns {"file_path" : "aaa/bbb/cccs"}

#Query Parameters
@app.get("/wishme")
async def wish_me(name: str = "your name"):
    return {"display" : f"welcome {name}"}

#Optional query parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# Multiple path and query parameters¶
"""You can declare multiple path parameters and query parameters at the same time, 
    FastAPI knows which is which.
    #And you don't have to declare them in any specific order."""
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
