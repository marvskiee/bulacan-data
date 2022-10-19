from os import defpath

from flask import render_template,url_for,redirect,request
# from werkzeug.utils import redirect
from app import app
from app.models import *
from app import db

import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview_data/<string:id>',)
def preview_data(id):
    students = Student.query.filter(Student.studentnumber==id).first()  
    return render_template("preview_data.html",students=students)
@app.route('/input_data_individually',methods=["POST","GET"])
def individual_data():
    grades=("1.00", "1.25", "1.50", "1.75", "2.00", "2.25", "2.50", "2.75", "3.00", "4.00", "5.00")
    schedules = ("7:00 AM - 10:00 AM","7:30 AM - 10:30 AM","8:00 AM - 11:00 AM","8:30 AM - 11:30 AM","9:00 AM - 12:00 PM","9:30 AM - 12:30 PM","10:00 AM - 1:00 PM","10:30 AM - 1:30 PM","11:00 AM - 2:00 PM","11:30 AM - 2:30 PM","12:00 PM - 3:00 PM","12:30 PM - 3:30 PM","1:00 PM - 4:00 PM","1:30 PM - 4:30 PM","2:00 PM - 5:00 PM","2:30 PM - 5:30 PM","3:00 PM - 6:00 PM","3:30 PM - 6:30 PM","4:00 PM - 7:00 PM","4:30 PM - 7:30 PM","5:00 PM - 8:00 PM")
    if request.method == 'POST':
        fr = request.form   
        print(fr)
        try:
            if len(fr['fullname']) > 0 and len(fr['year']) > 0 and len(fr['section']) > 0 and len(fr['email']) > 0 and len(fr['province']) > 0 and len(fr['municipality']) > 0 and len(fr['studentnumber']) > 0 and len(fr['studentclassification']) > 0 :
                student = Student(fullname=fr['fullname'], year=fr['year'], section=fr['section'],email=fr['email'],province=fr['province'],municipality=fr['municipality'],studentnumber=fr['studentnumber'],studentclassification=fr['studentclassification'],gradep1 = fr["gradep1"],
                gradep2 = fr['gradep2'],
                gradeop1 = fr['gradeop1'],
                gradeop2 = fr['gradeop2'],
                gradedata = fr['gradedata'],
                schedp1 = fr['schedp1'],
                schedp2 = fr['schedp2'],
                schedop1 = fr['schedop1'],
                schedop2 = fr['schedop2'],
                scheddata = fr['scheddata'])
                db.session.add(student)
                db.session.commit()
                id = fr['studentnumber']
                return redirect(f'/preview_data/{id}')
            raise TypeError("Only integers are allowed")
        except TypeError as e:
            return render_template('input_data_individually.html',success=False, isDuplicate=False, submitted=True, grades=grades, schedules=schedules)
        except Exception as e:
            print(e)
            return render_template('input_data_individually.html',success=False, isDuplicate=True, submitted=True, grades=grades, schedules=schedules)
    return render_template('input_data_individually.html',submitted=False,grades=grades, schedules=schedules)


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