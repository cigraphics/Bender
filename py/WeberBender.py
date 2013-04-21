#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import re as RegExp

from Brain import Brain

benderBrain = Brain()

class WeberBenderHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == "/":
            self.path = "/www/BenderBrain.html"
        if self.path == "/?up=forward/":
            benderBrain.moveForward()
        if self.path.startswith("/?left=left"):
            getDelay = RegExp.search("leftMotorDelay=(.+?)/", self.path)
            if getDelay:
                delay = getDelay.group(1)
                benderBrain.moveLeft(delay)
        if self.path.startswith("/?right=right"):
            getDelay = RegExp.search("rightMotorDelay=(.+?)/", self.path)
            if getDelay:
                delay = getDelay.group(1)
                benderBrain.moveRight(delay)
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
        

Handler = WeberBenderHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()
