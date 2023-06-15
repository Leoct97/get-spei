from main import df 
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_suc():
    return df