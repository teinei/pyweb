# from IPython.core import ipapi
# from sqlite3 import connect
# hist = ipapi.get().history_manager
# hist.db = connect(hist.hist_file, check_same_thread=False)

from flask import Flask

# old code
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db = SQLAlchemy(app)
#
engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind=engine
#
DBSession = sessionmaker(bind=engine)
session=DBSession()

@app.route('/')
@app.route('/hello')
def HelloWorld():
    # restaurant = db.session.query(Restaurant).first()
    restaurant = session.query(Restaurant).first()
    # items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output=''
    for i in items:
        output += i.name
        output += '<br>'
        output += i.price
        output += '<br>'
        output += i.description
        output += '<br>'
        output += '<br>'
    #
    return output

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
# type the following in browser
# http://localhost:5000/hello