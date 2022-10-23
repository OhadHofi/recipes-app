from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routers import players_api, recipes_api
import uvicorn

app = FastAPI()
app.include_router(players_api.router)
app.include_router(recipes_api.router)


app.mount("/client/build", StaticFiles(directory="client/build"), name="static")


@app.get("/")
def root():
    return FileResponse("./client/build/index.html")


@app.get('/sanity')
def sanity():
    return "OK"


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
