from fastapi import FastAPI

app = FastAPI()

#Path Parameters and Numeric Validations
@app.get('/item/{item_id}')
async def get_item(item_id: int):
    return {'item_id': item_id}