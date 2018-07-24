'''
print all names in db restaurants
print first restaurant's name
'''
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

# turn off same thread, or it will throw an error
engine = create_engine('sqlite:///restaurantmenu.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/hello')
def HelloWorld():
    # restaurants = session.query(Restaurant).all() # code for print all
    restaurant = session.query(Restaurant).first() # code for print one
    output = ''
    output += restaurant.name # code for print one
    output += '<br>'
    output += str(restaurant.id) # cast int to string
    output += '<br>' # code for print one
    
    # print all items in db 1
    # it doesn't work before, but after I delete old db and create new, it works now
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    for i in items:
        output += i.name
        output += '</br>'
    '''
    # code for print all
    for i in restaurants:
        output += i.name
        output += '</br>'
        # output += i.price
        # output += '</br>'
        # output += i.description
        # output += '</br>'
        # output += '</br>'
    '''
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
