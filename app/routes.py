from os import defpath

from flask import render_template,url_for,redirect
# from werkzeug.utils import redirect
from app import app
from app.models import *
from app import db

import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input_data_individually')
def individual_data():
    return render_template('input_data_individually.html')

@app.route('/import_data')
def import_data():
    return render_template('import_data.html')

@app.route('/cluster_visualization')
def cluster_visualization():
    return render_template('cluster_visualization.html')

@app.route('/cluster_graph')
def cluster_graph():
    return render_template('cluster_graph.html')

@app.route('/morning_graph')
def morning_graph():
    return render_template('morning_graph.html')

@app.route('/afternoon_graph')
def afternoon_graph():
    return render_template('afternoon_graph.html')

@app.route('/evening_graph')
def evening_graph():
    return render_template('evening_graph.html')


# @app.route('/')
# def index():
#     if Songs.query.count() < 1:
#         with open('phchords.json') as f:
#             data = json.load(f)
#         for d in data:
#             song = Songs(mode=d['mode'], artist=d['artist'], chords=d['chords'], title=d['title'],lyrics=d['lyrics'])    
#             db.session.add(song)
#         db.session.commit()
#     return render_template('index.html')

# @app.route('/search/<string:song>',methods=['POST','GET'])
# def song(song):
#     result = Songs.query.filter(Songs.title.like(f'%{song}%')).all()
#     return render_template('search.html',result=result)
# @app.route('/request')
# def show():
#     result = Request.query.all()
#     return render_template('request.html',result=result)

# @app.route('/request/<string:data>/<string:status>',methods=['POST','GET'])
# def request(data,status):
#     req = Request(data=data,status=status)
#     db.session.add(req)
#     db.session.commit()
#     result = Request.query.all()
#     return redirect('/request')