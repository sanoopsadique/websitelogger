
from http.server import BaseHTTPRequestHandler, HTTPServer
import sys

hostName = ""
serverPort = 80
refresh = sys.argv[1]

class MyServer(BaseHTTPRequestHandler): 
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Website Status</title><meta http-equiv=\"refresh\" content=\""+refresh+"\"></head>", "utf-8"))
        filePath = self.path[1:]
        if filePath == '':
            filePath = "status"
        self.wfile.write(bytes("<body>", "utf-8"))
        with open(filePath) as f:	
            for line in f:
                self.wfile.write(bytes(line, "utf-8"))
                self.wfile.write(bytes("</br>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    
    webServer = HTTPServer((hostName, serverPort), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")