# -*- coding:utf-8 -*-

import json

from flask import Flask, request, render_template
import os
from os.path import isfile, join

app = Flask(__name__)
listvideo = os.listdir("static/video")
percent = 100/(len(listvideo))
app.debug = True



@app.route('/wip')
def wip():    
    return render_template('indexwip.html',listvideo=listvideo, percent= percent)

@app.route('/porto')
def porto():    
    return render_template('indexPorto.html',listvideo=listvideo, percent= percent)

@app.route('/multi')
def multi():    
    return render_template('indexmulti.html',listvideo=listvideo, percent= percent)

@app.route('/')
def index():
    urltitle = [ { 'url':"/wip", 'title':"together "},
    { 'url':"/porto", 'title':"portfolio "},
    { 'url':"/multi", 'title':"multi "}
    ]    
    return render_template('index.html',listvideo=listvideo, urltitle=urltitle)

if __name__ == '__main__':
    app.run(host='0.0.0.0')