from typing import Union
from fastapi import FastAPI
import uvicorn
import json
import os
import requests
import geojson
from owslib.wfs import WebFeatureService
from owslib.wcs import WebCoverageService
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "this is Fast API"}


@app.get("/info")
def read_root():
    return {"Developer": ""}


@app.get("/usage")
def read_root():
    return {
        "/info": "Return the infos of the server application",
        "/usage": "Return the usage of the server application",
    }
