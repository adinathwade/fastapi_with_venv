from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


#Query Parameters and String Validations
@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(min_length=8, max_length=50)] = "sample defualt value"):
# async def read_items(q: Annotated[str | None, Query(min_length=8, max_length=50)] = None):
# async def read_items(q: str | None = Query(default = None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({'q': q})
    return results

#Query parameter list / multiple values
@app.post('/list/')
async def get_list(q: list[str]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({'q': q})
    return results
