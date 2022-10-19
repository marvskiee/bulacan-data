from enum import unique
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50),nullable=False)
    year =  db.Column(db.String(20), nullable=False)
    section =  db.Column(db.String(20), nullable=False)
    email =  db.Column(db.String(50), nullable=False)
    province =  db.Column(db.String(20), nullable=False)
    municipality =  db.Column(db.String(20), nullable=False)
    studentnumber =  db.Column(db.String(20), unique=True, nullable=False)
    studentclassification =  db.Column(db.String(20), nullable=False)
    gradep1 =  db.Column(db.String(20), nullable=True)
    gradep2 =  db.Column(db.String(20), nullable=True)
    gradeop1 =  db.Column(db.String(20), nullable=True)
    gradeop2 =  db.Column(db.String(20), nullable=True)
    gradedata =  db.Column(db.String(20), nullable=True)
    schedp1 =  db.Column(db.String(20), nullable=True)
    schedp2 =  db.Column(db.String(20), nullable=True)
    schedop1 =  db.Column(db.String(20), nullable=True)
    schedop2 =  db.Column(db.String(20), nullable=True)
    scheddata =  db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"{self.id}, {self.fullname}, {self.year}, {self.section}, {self.email}, {self.province },{self.municipality},{self.studentnumber}, {self.studentclassification},{self.gradep1}"
