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
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/new' >"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'> "
                output += "<input type='submit' value='Create'>"#value'Create' miss an '=' equal sign
                output += "</form></body></html>"
                self.wfile.write(output)
                return
            #
            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                #self.send_response(200)
                #self.send_header('Content-type', 'text/html')
                #self.end_headers()
                output = ""
                # objective 3 step 1, a link to create new 
                output += "<a href= '/restaurants/new'> Make a New Restaurant Here </a><br><br>"

                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                #
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name 
                    output += "<br>"                    
                    # objective 2
                    output += "<a href='#'>Edit</a>"
                    output += "<br>"
                    output += "<a href='#'>Delete</a>"
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
            if self.path.endswith("/restaurants/new"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form=data':
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