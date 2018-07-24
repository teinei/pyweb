# webserver-crud-jo.2.py
# restaurants crud
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi # I forget to import cgi
# import depandencies
# import crud operations from lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# create session and connect to db
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

# handler
class WebServerHandler(BaseHTTPRequestHandler):
    # handle get request
    def do_GET(self):
        try:
            # objective 3 step 2, creat /restaurants/new page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant(do get)</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new' >"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'> "
                output += "<input type='submit' value='Create'>"#value'Create' miss an '=' equal sign
                output += "</form></body></html>"
                self.wfile.write(output)
                return
            #
            if self.path.endswith("/edit"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += myRestaurantQuery.name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/edit'> " % restaurantIDPath
                    output += "<input name='newRestaurantName' type='text' placeholder='%s' >"% myRestaurantQuery.name
                    output += "<input type='submit' value='Rename'  >"
                    output += "</form>"
                    output += "</body></html>"

                    self.wfile.write(output)
                #
            #
            if self.path.endswith("/delete"):
                restaurantIDPath=self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myRestaurantQuery:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s?" % myRestaurantQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/%s/delete' >" % restaurantIDPath
                    output += "<input type='submit' value='Delete' >"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
            #
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                #self.send_response(200)
                #self.send_header('Content-type', 'text/html')
                #self.end_headers()
                output = ""
                # objective 3 step 1, a link to create new 
                output += "<a href= '/restaurants/new'> Make a New Restaurant Here(link) </a><br><br>"

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name 
                    output += "<br>"                    
                    # objective 2
                    # objective 4 replace hash tag with 
                    output += "<a href='/restaurants/%s/edit'>Edit</a>" % restaurant.id
                    output += "<br>"
                    # objective 5 -- replace delete href
                    output += "<a href='/restaurants/%s/delete'>Delete</a>" % restaurant.id
                    output += "<br><br><br>"
                    #
                output += "</body></html>"
                self.wfile.write(output)
                return
                #
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
            # error

    # post handler
    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                restaurantIDPath = self.path.split("/")[2]
                myRestaurantQuery = session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                if myRestaurantQuery:
                    session.delete(myRestaurantQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type','text/html')
                    self.send_header('Location','/restaurants')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype=='multipart/form-data':
                    fields=cgi.parse_multipart(self.rfile,pdict)
                    messagecontent=fields.get('newRestaurantName')
                    restaurantIDPath=self.path.split("/")[2]

                    myRestaurantQuery=session.query(Restaurant).filter_by(id=restaurantIDPath).one()
                    if myRestaurantQuery != []:
                        myRestaurantQuery.name = messagecontent[0]
                        session.add(myRestaurantQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type','text/html')
                        self.send_header('Location','/restaurants')
                        self.end_headers()
            #
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data': # form=data here
                    #
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newRestaurantName')

                    # create new restaurant object
                    newRestaurant = Restaurant(name=messagecontent[0])
                    session.add(newRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type','text/html')
                    self.send_header('Location','/restaurants')
                    self.end_headers()
                    #
                #
                #
        except:
           pass


# main method
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        # define server
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()
        # shutdown server

if __name__ == '__main__':
    main()