#create
#import dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import self defined classes
from database_setup import Base, Restaurant, MenuItem

# which engine we use, bind engine to base class
engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine

# create session maker, establish a link between 
# our code and engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

# add new entry, it will be added until commit
myFirstRestaurant = Restaurant(name="Pizza place")
session.add(myFirstRestaurant)
session.commit()

# query to see if it is added
session.query(MenuItem).all()

# add menu item, specity its attributes
cheesepizza=MenuItem(name="Cheese Pizza", description="Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99",restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()

# query to see if its there
session.query(MenuItem).all()

# read
firstResult=session.query(Restaurant).first()
firstResult.name

# compile and print items in lotsofmenus.py
# python lotsofmenus.py
items=session.query(Restaurant).all() 
for item in items:
    print item.name
# 
