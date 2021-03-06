from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import SonosControl

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

##    def do_GET(self):
##        s = SonosControl.getStatus()
##        if s == "PLAYING":
##            SonosControl.pause()
##            self.send_response(808)
##            self.send_header('Content-type', 'text/html')
##            self.end_headers()
##            print "paused"
##        else:
##            SonosControl.play()
##            self.send_response(505)
##            self.send_header('Content-type', 'text/html')
##            self.end_headers()
##            print "playing"
##        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        request_path = self.path

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        text = request_headers.getheaders('Data')
        locate = request_headers.getheaders('Location')
        print locate
        if text[0]=='Sync':
            SonosControl.setZoneVolumeEqual()
            #ADD Play same song
        if locate[0] =="ALL":
            print (text)
            if text[0]=='Play':
                SonosControl.playAll()
                print "playing"
            elif text[0]=='Pause':
                SonosControl.pauseAll()
                print "paused"
            elif text[0]=='Volume+':
                SonosControl.volumeUpAll()
            elif text[0]=='Volume-':
                SonosControl.volumeDownAll()
            elif text[0]=='Next':
                SonosControl.play_nextAll()
            elif text[0]=='Prev':
                SonosControl.play_previousAll()
            elif text[0]=='IsPlaying':
                self.send_response(200 + SonosControl.isPlayingAll())
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return
            else:
                print "Not programmed"
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        else:
            print (text)
            if text[0]=='Play':
                SonosControl.play(locate[0])
                print "playing " + locate[0]
            elif text[0]=='Pause':
                SonosControl.pause(locate[0])
                print "paused"
            elif text[0]=='Volume+':
                SonosControl.volumeUp(locate[0])
            elif text[0]=='Volume-':
                SonosControl.volumeDown(locate[0])
            elif text[0]=='Next':
                SonosControl.play_next(locate[0])
            elif text[0]=='Prev':
                SonosControl.play_previous(locate[0])
            elif text[0]=='IsPlaying':
                self.send_response(200 + SonosControl.isPlaying(locate[0]))
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return
            else:
                print "Not programmed"
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

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
