# -*- coding:utf-8 -*-

import json

from flask import Flask, request, render_template
import os
from os.path import isfile, join

app = Flask(__name__)

app.debug = True
@app.route('/')
def index():
    listvideo = os.listdir("static/video")
    return render_template('indexOk.html',listvideo=listvideo)

if __name__ == '__main__':
    app.run(host='0.0.0.0')