# -*- coding:utf-8 -*-

import json

from flask import Flask, request, render_template
import os
from os.path import isfile, join

app = Flask(__name__)
listvideo = os.listdir("static/video")
percent = 100/(len(listvideo))
app.debug = True

@app.route('/compare/<index1>/<index2>')
def compare(index1,index2):    
    return render_template('compare.html',listvideo=listvideo,video1=listvideo[int(index1)],video2=listvideo[int(index2)])


@app.route('/wip')
def wip():    
    return render_template('indexwip.html',listvideo=listvideo, percent= percent)

@app.route('/multi')
def multi():    
    return render_template('indexmulti.html',listvideo=listvideo, percent= percent)

@app.route('/')
def index():
    urltitle = [ { 'url':"/wip", 'title':"together "},
    { 'url':"/multi", 'title':"multi "}]

    for index in range(len(listvideo)):
        for i in range(index+1, len(listvideo)): 
           urltitle.append({ 'url':"/compare/%d/%d" % (index,i), 'title':"compare %d et %d" % (index,i)})
        
    return render_template('index.html',listvideo=listvideo, urltitle=urltitle)

if __name__ == '__main__':
    app.run(host='0.0.0.0')