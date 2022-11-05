
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os, datetime


hostName = ""
serverPort = 80
service = ""
refresh = 5

class MyServer(BaseHTTPRequestHandler): 
    def do_GET(self):
        global service
        global refresh
        self.send_response(200)
        status = os.popen("systemctl is-active "+service).read().rstrip()
        if status =="active":
            color = "green"
        else:
            color = "red"
        now = datetime.datetime.now() 
        msg = "<a style=\"color:"+color+";\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+service+" is "+status+"</a>\n"
        with open("status","rt") as f:
            for line in f:
                msg = msg+line
        with open("status","wt") as f:
            f.write(msg)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>SMART Status</title><meta http-equiv=\"refresh\" content=\""+str(refresh)+"\"></head>", "utf-8"))
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
    while True:
        service = input("Enter service name: ")
        if service == '':
            continue
        status = os.popen("systemctl is-active "+service).read().rstrip()
        if status == 'unknown':
            print(service + " not installed, Please try again")
        else:
            with open("status","wt") as f:
                f.write("")
            break
    refresh = input("Enter refresh time in seconds[default = 3]: ")
    if type(refresh) == float:
        refresh = int(refresh)+1
    elif type(refresh) != int:
        refresh = 3
    if refresh < 0:
        refresh = -1 * refresh
    print("Page will auto-refresh in "+ str(refresh)+" seconds")
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started. Visit http://ip-address:%s" % serverPort)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")