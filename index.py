
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import re
import spacy
import json



app = Flask(__name__)


@app.route('/')
def handle_request():
    return "asdd"

