from fastapi import FastAPI, Path, Query

app = FastAPI()

#Path Parameters and Numeric Validations
@app.get("/items/{itemid}")
async def getitems(
    id: int = Path(default=1), 
    q: str | None= Query(default=..., )
):
    return "something"

#Number validations: greater than and less than or equal
@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# declare metadata -- see docs
# https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#declare-metadata
