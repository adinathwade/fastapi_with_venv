from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None


@app.post('/item')
async def request_body(item : Item):
    print(item.name, item.description, item.price, item.tax)
    item_dict = item.dict()
    print('item dict: ',item_dict)
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return {'message': 'request body demo.....', 'item': item_dict}

#Request body + path parameters
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

#Request body + path + query parameters
@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return {'result': result}