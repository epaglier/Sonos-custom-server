from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import SonosControl

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        s = SonosControl.getStatus()
        if s == "PLAYING":
            SonosControl.pause()
            self.send_response(808)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print "paused"
        else:
            SonosControl.play()
            self.send_response(505)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            print "playing"
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()