from fastapi import FastAPI

app = FastAPI()

# first match will execute for the get api always
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]