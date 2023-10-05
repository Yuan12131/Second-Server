import http.server
import socketserver


class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = './230913_training.html'
        else:
            self.send_response(200)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyServer

PORT = 8080

my_server = socketserver.TCPServer(("",PORT), handler_object)
my_server.serve_forever()