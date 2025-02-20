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

class FruitEnum:
    def __init__(self):
        self.fruit = 'fruit'
        self.vegetable = 'vegetable'
        self.dairy = 'dairy'

fruit = FruitEnum()

@app.get("/fruit/{fruit_item}")
async def get_fruit_item(fruit_item: str):
    if fruit_item == fruit.fruit:
        return {'food': fruit_item, 'message': 'health for living...'}



'''
to run app:
$uvicorn test:app --reload
'''