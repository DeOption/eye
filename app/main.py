import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import uvicorn
from fastapi import FastAPI

from app.api.api_v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )


if __name__ == "__main__":
    uvicorn.run(app=app, host='127.0.0.1', port=8000)
