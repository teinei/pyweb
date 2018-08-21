from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup_rise import Base, Survey, WeeklyReport, RiseClass
#
# connect to db, setup db name
engine=create_engine('sqlite:///rise.db?check_same_thread=False')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#
from numpy import genfromtxt
from datetime import date,datetime
#

#------------
#read-csv.py
import csv

def dateConverter(phpdate):
    pydate=phpdate.split('-')
    #print pydate
    return pydate

def list2date(pylist=list('123')):
    counter1 = 0
    year=2011
    month=1
    day=1
    print '\n------------------------------------'
    print "pylist in list2date : "+str(pylist)
    #
    #
    for item in pylist:
        print "\nin list2date item is : "+item
        #counter1 = 0
        counter2=pylist.index(item)
        print 'counter1 is: '+str(counter1)+'\n'
        if counter1 == 0: 
            #print "counter1 == 0"
            #print item
            year = int(item)
            print "year is : "+str(year)
            #counter1 +=1
            #continue
        if counter1 == 1:
            #print "counter1 == 1"
            #print item
            month = int(item)
            print "month is: "+str(month)
            #counter1 +=1
            #continue
        if counter1 == 2:
            #print "counter1 == 2"
            #print item
            day = int(item)
            print 'day is : '+str(day)
            #counter1 +=1
            print "---"
            #continue
        #counter2 += 1
        counter1 +=1
    print '\nyear is : '+str(year)
    print 'month is: '+str(month)
    print 'day is: '+str(day)
    #now = datetime.now()
    #print str(now)
    #
    if year==0 and month==0 and day==0:
        year = 2011
        month = 1
        day = 1
    pydate=date(year,month,day)
    return pydate

def readCSV():
    with open('rise-classes.csv','rb') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',')
        lineCount=0
        for row in csvReader:
            print 'this is a row, this is a rise class'
            counter=0
            for item in row:
                counter +=1
                #print "this is the #"+str(counter)+" item in row"
                #print item
                #print "\n"
                #print "where is the - : "+str(item.find('-'))
                if item.find('-')>0 and item.find('-')==4:
                    #print "\nstart of if"
                    #print "\n"
                    #pydate = dateConverter(item)
                    pylist =dateConverter(item)
                    for x in pylist:
                        print x
                        print 'index of '+str(pylist.index(x))
                    #print "length of item: "+str(len(item))
                    #print type(item)
                    #for x in pydate:
                    #    #print x
                    #    print 'index of '+str(pydate.index(x))
                    #    print x
                    #pydate2 = date(pydate[0],pydate[1],pydate[2])
                    pydate = list2date(pylist)
                    #
                    #pydate2 = list2date(pydate)
                    print "python date is : "+str(pydate)
                    #print "end of if\n"
                    #print '------------------------------------'
                    print '************************************'
                    #
            print '===================================='
    #return render_template('read-csv.html')

#readCSV()

#
def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skiprows=1, converters={0: lambda s: str(s)})
    return data.tolist()
#


def add2DB(record):
    #vars to handle date, open
    startDate=record['start_date']
    openi = record['open1']
    openii = record['open2']
    openiii = record['open3']
    graduateDate = record['graduate_date']
    
    startDate_list=dateConverter(startDate)
    openi_list=dateConverter(openi)
    openii_list=dateConverter(openii)
    openiii_list=dateConverter(openiii)
    graduateDate_list=dateConverter(graduateDate)

    startDate_py=list2date(startDate_list)
    openi_py=list2date(openi_list)
    openii_py=list2date(openii_list)
    openiii_py=list2date(openiii_list)
    graduateDate_py=list2date(graduateDate_list)
    #vars to handle date, close
    classNameRaw=record['class_name']
    print classNameRaw
    
    classItem1 = RiseClass(
        class_stage=record['class_stage'],
        class_name=record['class_name'], 
        main_teacher=record['main_teacher'],
        teaching_assistant=record['help_teacher'],
        start_date=startDate_py,
        open1=openi_py, 
        open2=openii_py, 
        open3=openiii_py, 
        graduate_date=graduateDate_py
    )

    session.add(classItem1)
    session.commit()

def readCSV(file_name="rise-classes.csv"):
    csvdata = list()
    with open(file_name,'rb') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',')
        print csvReader
        for i in csvReader:	
            record = { # its a dictionary
                'class_stage': i[2], 
                'class_name': i[3], 
                'main_teacher': i[4], 
                'help_teacher': i[5],  
                'start_date': i[6],  
                'open1': i[7],  
                'open2': i[8],  
                'open3': i[9],  
                'graduate_date': i[10]
            }
            csvdata.append(record)
        #        
    #
    print '\n'
    #print csvdata
    for row in csvdata:
        print '\n'
        print row
        for key,value in row.items():
            print value
    return csvdata
    
def printReadedData(csvdata):
    for row in csvdata:
        print '\nprint out row'
        print row
        counter = 1
        for key,value in row.items():
            print 'print out value #'+ str(counter)+ ' : ' +str(value)
            #print value
            counter += 1
    #return csvdata

def writeCSV2DB():
    file_name="rise-classes.csv"
    with open(file_name,'rb') as csvFile:
        csvReader = csv.reader(csvFile,delimiter=',')
        lineCount=0
        #
        for i in csvReader:	
            record = { # its a dictionary
                'class_stage': i[2], 
                'class_name': i[3], 
                'main_teacher': i[4], 
                'help_teacher': i[5],  
                'start_date': i[6],  
                'open1': i[7],  
                'open2': i[8],  
                'open3': i[9],  
                'graduate_date': i[10]
            }
            if record['start_date'].find('-')>0:
                print "\nrecord['class_name'] is:"
                className=record['class_name']
                print className
                isExist = ifExist(className)
                print 'class isExist: '
                print isExist
                if isExist != 1:      
                    add2DB(record)
    print "\ndone"
#readCSV2DB2()



def ifExist(class_name):
    isExist = 0
    existClasses=session.query(RiseClass).all()
    for classn in existClasses:
        if class_name ==classn.class_name:
            #print 'class exist'
            isExist = 1
    #
    return isExist

def updateDB():
    csvdata = readCSV()
    #printReadedData(csvdata)
    #
    for classn in csvdata:
        className = classn['class_name']
        open1=classn['open1']
        #print className

        existClasses=session.query(RiseClass).all()
        for classm in existClasses:
            dbopen1 = classm.open1
            dbClassName = classm.class_name
            dbClassId = classm.id

            #
            newName = dbClassName[-2:]
            #print newName
            print 'old name is : '+str(dbClassName)
            print 'new name is : '+str(newName)
            classm.class_name = newName

            #
            session.add(classm)
            session.commit()
            #


            #print 'dbClassId is : '+str(dbClassId)



            #editedClass = session.query(RiseClass).filter_by(id=dbClassId).one()
            #print editedClass.class_name

            #print '\n'
            #print 'class name is : '+dbClassName
            #print classm
            #print dbopen1
        #print '\n'

        
    #
    print "\n db updated"

def run():
    print 'something ro run'
    #
    #readCSV()
    updateDB()
    #writeCSV2DB()
    #

run()