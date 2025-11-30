"""Fast api app."""

from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get(path="/")
def hello() -> dict[str, str]:
    now: datetime = datetime.now()
    return {"Hello": now.strftime(format=r"%d/%m/%Y, %H:%M:%S")}


# uvicorn main: app
