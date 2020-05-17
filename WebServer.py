#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep, path
PORT_NUMBER = 8080
#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
        def do_GET(self):
                #Add your checking of the self.path equals to "/"
                if (self.path == "/" and path.isfile("index.html")):
                        self.path = "/index.html"
                if self.path == "/index":
                        self.path = "/index" + ".html"
                if self.path == "/index.htm":
                        self.path = "/index.html"
                # Add your code below for various content types
                try:
                    #Check the file extension required and
                    #set the right mime type
                        sendReply = False
                        if self.path.endswith(".html"):
                                 mimetype='text/html'
                                 sendReply = True
                        # add more code here for various image types
                        if self.path.endswith(".jpg"):
                                mimetype='image/jpeg'
                                sendReply = True
                        if self.path.endswith(".gif"):
                                mimetype = 'image/gif'
                                sendReply = True
                        if self.path.endswith(".js"):
                                 mimetype ='application/javascript'
                                 sendReply = True
                        if self.path.endswith(".css"):
                                mimetype = 'text/css'
                                sendReply = True


                        if sendReply == True:
                            #Open the static file requested and send it
                                f = open(curdir + sep + self.path, "rb")
                                self.send_response(200)
                                self.send_header('Content-type',mimetype)
                                self.end_headers()
                                self.wfile.write(f.read() )
                                f.close()
                except IOError:
                        # change the code to send an error web page dynamically
                        self.send_error(404,'File Not Found:%s'%self.path)
        #Using the post method to move to result.html dynamically to display the information about the order
        def do_POST(self):
                try:
                    #Check the file extension required and
                    #set the right mime type
                        sendReply = False
                        if self.path.endswith(".html"):
                                 mimetype='text/html'
                                 sendReply = True
                        # add more code here for various image types
                        if self.path.endswith(".jpg"):
                                mimetype='image/jpeg'
                                sendReply = True
                        if self.path.endswith(".gif"):
                                mimetype = 'image/gif'
                                sendReply = True
                        if self.path.endswith(".js"):
                                 mimetype ='application/javascript'
                                 sendReply = True
                        if self.path.endswith(".css"):
                                mimetype = 'text/css'
                                sendReply = True
                        if sendReply == True:
                            #Open the static file requested and send it
                                f = open(curdir + sep + self.path, "rb")
                                self.send_response(200)
                                self.send_header('Content-type',mimetype)
                                self.end_headers()
                                self.wfile.write(f.read() )
                                f.close()
                        return

                except IOError:
                        # change the code to send an error web page dynamically
                        self.send_error(404,'File Not Found:%s'%self.path)
# main routine starts here - no need to change this part
try:
                #Create a web server and define the handler to manage the
                #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print ('Started httpserver on port ' , PORT_NUMBER)

        #Wait forever for incoming htto requests
        server.serve_forever()
except KeyboardInterrupt:
        print ('^C received, shutting down the web server')
        server.socket.close()
