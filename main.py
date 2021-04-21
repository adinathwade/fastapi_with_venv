from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'greeting': 'good morning'}

@app.get('/about')
def about():
    return {'data': 'this is about'}