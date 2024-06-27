from typing import Union

from fastapi import FastAPI, status

from router.router import router as public_router
from config.config import APP_DESCRIPTION, APP_NAME, APP_VERSION
from config.response import SuccessfulResponseModel

app = FastAPI(title=APP_NAME, description=APP_DESCRIPTION, version=APP_VERSION)


app.include_router(public_router, prefix="/api")

@app.get("/", status_code=status.HTTP_200_OK, tags=["default".upper()])
def read_root():
    return SuccessfulResponseModel(message="API is running...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug")
