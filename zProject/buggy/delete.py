# delete.py
# import dependencies
# alt+z to wrap/raep/ text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import self defined classes
from database_setup import Base, Restaurant, MenuItem

# which engine we use, bind engine to base class
engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine

# create session maker, establish a link between 
# our code and engine
DBSession=sessionmaker(bind=engine)
session=DBSession()
# that's all to prepare

# find spinach ice
spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
print spinach.restaurant.name

# delete it
session.delete(spinach)
session.commit()

# test if we can print spinach out
# spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
