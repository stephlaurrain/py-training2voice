# -*-coding:utf-8 -*

import os
from os import path
import sys
import random
from datetime import datetime
from time import sleep
import inspect
import utils.file_utils as file_utils
import utils.mylog as mylog
import utils.jsonprms as jsonprms
from utils.mydecorators import _error_decorator
from fastapi import FastAPI
import uvicorn
import colorama as colorama

app = FastAPI()

@app.get("/")
def index():
        return {"message": "Hello World"}

if __name__=='__main__':
        colorama.init()
        uvicorn.run(app, host="127.0.0.1", port=8000)
