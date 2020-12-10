import uvicorn

from fastapi import FastAPI

from app.api.api_v1.api import api_router

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
