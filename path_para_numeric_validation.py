from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

#Path Parameters and Numeric Validations
@app.get('/item/{item_id}')
async def get_item(item_id: int):
    return {'item_id': item_id}

@app.get('/items/{item_id}')
async def get_item(item_id: Annotated[int, Path(title='this is path para')],
                   q: Annotated[str, Query(title='this is query para', min_length=8, max_length=30)] = None):
    return {'item_id': item_id, 'q': q}

@app.get("/item_validate/{item_id}")
async def item_validate(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=10)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results