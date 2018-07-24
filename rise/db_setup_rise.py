# file: db_setup_rise.py
# db type ref
# http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
'''
db design
table: survey
colums: 
id, open_date, ordinal, main_teacher, teaching_assistant,
q1,q2,q3,q4,q5,average
q11, text1, text2, text3,
student_name/student_id,
class_name/class_id,
tel

table: weekly_report
id, class_name, open_date, 
main_teacher,teaching_assistant,
average, text1, text2, text3

table: class
id, class_stage, class_name,
main_teacher, teaching_assistant,
start_date, open1, open2, open3, graduate_date
'''
import sys
#
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#
#from datetime import datetime
import datetime

Base=declarative_base()

engine=create_engine('sqlite:///rise.db')
Base.metadata.create_all(engine)


class Survey(Base): #table: survey
    __tablename__='survey' #colums:
    id=Column(Integer, primary_key=True) #id
    #open_date=Column(DateTime, nulltable=False, default=datetime.date.today) #open_date
    open_date=Column(DateTime)
    ordinal=Column(Integer) #ordinal
    main_teacher=Column(String(80)) #main_teacher
    teaching_assistant=Column(String(80)) #TA
    #q1..q5, grade for teachers
    q1=Column(Integer)
    q2=Column(Integer)
    q3=Column(Integer)
    q4=Column(Integer)
    q5=Column(Integer)
    average=Column(Integer)
    # q11 will to pay
    q11=Column(Integer)
    text1=Column(Text)
    text2=Column(Text)
    text3=Column(Text)
    #student and class
    student_name=Column(String(80))    #student_name/student_id,
    class_id=Column(Integer,ForeignKey('rise_class.id'))
    class_name=Column(Integer) #class_name/class_id,
    tel=Column(Integer) #telephone/cellphone number
class WeeklyReport(Base):
    __tablename__ = 'weekly_report'
    id=Column(Integer,primary_key=True)
    class_name=Column(Integer)
    open_date=Column(DateTime)
    main_teacher=Column(String(80)) #main_teacher
    teaching_assistant=Column(String(80)) #TA
    average=Column(Integer)
    text1=Column(Text)
    text2=Column(Text)
    text3=Column(Text)
    # open_date=Column(DateTime, nulltable=False, default=datetime.utcnow)
class RiseClass(Base):
    __tablename__ = 'rise_class'
    id=Column(Integer,primary_key=True)
    class_stage=Column(String(80))
    class_name=Column(Integer,nullable=False)
    main_teacher=Column(String(80)) #main_teacher
    teaching_assistant=Column(String(80)) #TA
    start_date=Column(DateTime)
    open1=Column(DateTime)
    open2=Column(DateTime)
    open3=Column(DateTime)
    graduate_date=Column(DateTime)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }
'''    
table: class
id, class_stage, class_name,
main_teacher, teaching_assistant,
start_date, open1, open2, open3, graduate_date
'''
engine=create_engine('sqlite:///rise.db')
Base.metadata.create_all(engine)