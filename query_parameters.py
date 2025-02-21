from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

# first match will execute for the get api always
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


# query parameters
# http://127.0.0.1:8000/items/?skip=0&limit=10
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")  #'http://127.0.0.1:8000/items/?skip=1&limit=8'
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/item/name?q=hi'
@app.get('/item/{item_id}')
async def get_item(item_id: str, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Multiple path and query parameters
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