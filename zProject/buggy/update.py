# update.py

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
# that's all to prepare

veggieBurgers=session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
#
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=11).one()
print UrbanVeggieBurger.price
#
UrbanVeggieBurger.price='$5.99'
session.add(UrbanVeggieBurger)
session.commit()
#