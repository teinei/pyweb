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

def readCSV():
    with open('rise-classes.csv','rb') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',')
        lineCount=0
        for row in csvReader:
            print 'this is a row, this is a rise class'
            counter=0
            for item in row:
                print counter+1
                print item
                counter += 1
            print '------------------------------------'
    #return render_template('read-csv.html')

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


















                



