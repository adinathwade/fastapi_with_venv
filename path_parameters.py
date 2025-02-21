from fastapi import FastAPI

app = FastAPI()

# @app.get('/', description='this is first app', deprecated=True)
@app.get('/', description='This is first app')
async def get():
    return {'Name': 'Adinath Wade.....'}
@app.post('/{id}')
async def post(id):
    return {'post': 'post method...', 'id': id}
#path parameters
@app.get('/{item}')
async def get_item(item: int):
    return {'Item': item}

from enum import Enum
class FruitEnum(str, Enum):
    fruit = 'fruit'
    vegetable = 'vegetable'
    dairy = 'dairy'

@app.get("/fruit/{fruit_item}")
async def get_fruit_item(fruit_item: FruitEnum):
    if fruit_item == FruitEnum.fruit:
        return {'food': fruit_item, 'message': 'health for living...'}
    if fruit_item == FruitEnum.vegetable:
        return {'food': fruit_item, 'message': 'vegetables health for living...'}
    return {'dairy': FruitEnum.dairy, 'message': 'dairy products are healthy for body'}



'''
to run app:
$uvicorn test:app --reload
'''