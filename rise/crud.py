# file: crud.py
# from flask import render_template, url_for
# url_for('functionName',arg_name=value)
# render_template('somename.html',arg_name=value)
import csv
#import csv lib to read csv
from datetime import date,datetime
import datetime
#
from flask import Flask,render_template,url_for,request,redirect
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#
from db_setup_rise import Base, Survey, WeeklyReport, RiseClass
#
# connect to db, setup db name
engine=create_engine('sqlite:///rise.db?check_same_thread=False')
Base.metadata.bind=engine
# session
DBSession=sessionmaker(bind=engine)
session=DBSession()
# create app
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def showAll():
    return render_template('home.html')
    # render_template() function?
    # function body
#

#
@app.route('/survey')
def showSurveys():
    surveys  = session.query(Survey).all()
    return render_template('survey-index.html',htmlSurveys=surveys)
    #

#function to add new survey
@app.route('/survey/new' , methods=['GET','POST'])
def newSurvey():
    if request.method == 'POST':
        
        py_class_stage = request.form['html_class_stage']
        classNameA = request.form['class_name_a']
        classNameB = request.form['class_name_b']
        py_class_name = classNameA+classNameB
        py_student_name = request.form['html_student_name']
        #
        # assign all post args to class
        newSurvey = Survey(db_class_stage=py_class_stage,class_name=py_class_name,student_name=py_student_name)
        # add to db
        # ------------
        # session.add(newSurvey)
        # session.commit()
        
        # return
        return render_template('newSurvey.html',py2html_class_stage=py_class_stage,py2html_class_name=py_class_name,py2html_student_name=py_student_name)
    else: 
        return render_template('newSurvey.html')
    
    #

@app.route('/class')
def showRiseClasses():
    htmlClasses = session.query(RiseClass).all()
    return render_template('class-index.html',htmlClasses=htmlClasses)
    #
#
@app.route('/class/read-csv')
def readCSV():
    return render_template('read-csv.html')
    #

#function to add new class
@app.route('/class/new',methods=['GET','POST'])
@app.route('/class/new/',methods=['GET','POST'])
def newClass():
    if request.method == 'POST': # from flask import request
        newClass = RiseClass(class_name=request.form['class_name'])
        session.add(newClass)
        session.commit()
        #return redirect(url_for('showRiseClasses'))
        return render_template('newClass.html')
    else:
        return render_template('newClass.html')
#
@app.route('/class/<int:class_id>/delete/', methods=['GET', 'POST'])
def deleteClass(class_id):
    classToDelete=session.query(RiseClass).filter_by(id=class_id).one()
    # I miss .one()
    if request.method=='POST':
        session.delete(classToDelete)
        session.commit()
        return redirect(url_for('showRiseClasses', class_id=class_id))
    else:
        return render_template('deleteClass.html',rise_class=classToDelete)

#
@app.route('/class/<int:class_id>/edit/', methods=['GET', 'POST'])
def editClass(class_id):
    editedClass = session.query(
        RiseClass).filter_by(id=class_id).one()
    if request.method == 'POST':
        if request.form['class_stage']:
            editedClass.class_stage = request.form['class_stage']
        #
        if request.form['class_name']:
            editedClass.class_name = request.form['class_name']
        #
        if request.form['d_teacher']:
            editedClass.main_teacher = request.form['d_teacher']
        #
        if request.form['co_teacher']:
            editedClass.teaching_assistant = request.form['co_teacher']
        #
        #gradu = datetime.date(year=2012,month=5,day=21)
        if (request.form['graduate_year'] and request.form['graduate_month'] and request.form['graduate_day']):
            year_form=request.form['graduate_year']
            month_form=request.form['graduate_month']
            day_form=request.form['graduate_day']
            year_int=int(year_form)
            month_int=int(month_form)
            day_int=int(day_form)
            editedClass.graduate_date = date(year_int,month_int,day_int)
            #print "<p>editedClass.graduate_date</p>"
            #gradu = str(editedClass.graduate_date)

        #
        session.add(editedClass)
        session.commit()
        #
        return redirect(url_for('showRiseClasses'))
        #return gradu
    else:
        return render_template(
            'editClass.html', riseClass=editedClass)
#
#@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
#def editRestaurant(restaurant_id):
#    editedRestaurant = session.query(
#        Restaurant).filter_by(id=restaurant_id).one()
#    if request.method == 'POST':
#        if request.form['name']:
            #
#            editedRestaurant.name = request.form['name']
#            return redirect(url_for('showRestaurants'))
#    else:
#        return render_template(
#            'editRestaurant.html', restaurant=editedRestaurant)

    # return 'This page will be for editing restaurant %s' % restaurant_id
#

#
#
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
#
#

