
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading


def errResponder(client):
    client.send_response(404)
    client.end_headers()
    client.wfile.write('\n')

def staticResponder(staticResourceName):
    staticBlob = open(staticResourceName,'rb').read()
    def responseFunc(client):
        client.send_response(200)
        client.end_headers()
        client.wfile.write(open(staticResourceName,'rb').read())
        client.wfile.write('\n')
    return responseFunc

def getMessagesResponder(client):
    client.send_response(200)
    client.end_headers()
    client.wfile.write( '[{},{}]' )
    client.wfile.write('\n')

routing = {
        '/':staticResponder('index.html'),
        '/style':staticResponder('style.css'),
        '/js':staticResponder('app.js'),
        '/messages':getMessagesResponder
}

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        handler = routing.get(self.path,errResponder)
        handler(self)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
