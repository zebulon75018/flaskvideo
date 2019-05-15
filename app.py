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
    percent = 100/(len(listvideo))
    return render_template('indexPorto.html',listvideo=listvideo, percent= percent)

if __name__ == '__main__':
    app.run(host='0.0.0.0')