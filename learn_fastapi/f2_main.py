from fastapi import FastAPI, Query

app = FastAPI()

#Query Parameters and String Validations

"""We are going to enforce that even though q is optional, 
whenever it is provided, its length doesn't exceed 50 characters"""
@app.get("/items")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#more validations
@app.get("/fitems")
async def filter_items(q: str | None =Query(default=None, max_length=10, min_length=2)):
    return {"query": q}

#define a regular expression that the parameter should match
@app.get("/items2/")
async def read_items2(
    q: str
    | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#making a query parameter required with "..." or "Required" or not having default value 
# "from pydantic import Required"                         -- see docs


#Query parameter list / multiple values - also can have defaults
@app.get("/items3/")
async def read_items3(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items

"""
query: http://localhost:8000/items/?q=foo&q=bar
response :
{
  "q": [
    "foo",
    "bar"
  ]
}
"""
#more metadata - alias - deprecated -- see docs
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata
