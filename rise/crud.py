# file: crud.py
# from flask import render_template, url_for
# url_for('functionName',arg_name=value)
# render_template('somename.html',arg_name=value)
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
def showClasses():
    return render_template('home.html')
    # render_template() function?
    # function body
#

@app.route('/class')
def showRiseClasses():
    htmlClasses = session.query(RiseClass).all()
    return render_template('class-index.html',htmlClasses=htmlClasses)
    #
#
@app.route('/class/new',methods=['GET','POST'])
def newClass():
    if request.method == 'POST': # from flask import request
        newClass = RiseClass(class_name=request.form['class_name'])
        session.add(newClass)
        session.commit()
        return redirect(url_for('showRiseClasses'))
        #redirect, why use redirect
        #
    else:
        return render_template('newClass.html')
        #
    #
    #
#
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
#
#

