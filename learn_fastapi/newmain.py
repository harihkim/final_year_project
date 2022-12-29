from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def root():
    return "send request body to /send"

#Request Body
@app.post("/items/")
async def create_item(item: Item):
    return item.name


# Request body + path parameters
"""FastAPI will recognize that the function parameters that match path parameters should 
be taken from the path, and that function parameters that are declared to be Pydantic 
models should be taken from the request body"""
@app.post("/itemsid/{item_id}")
async def create_item_with_id(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# Request body + path + query parameters
"""
If the parameter is also declared in the path, it will be used as a path parameter.
If the parameter is of a singular type (like int, float, str, bool, etc) 
    it will be interpreted as a query parameter.
If the parameter is declared to be of the type of a Pydantic model, 
    it will be interpreted as a request body.
"""
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
