
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os, datetime
import subprocess
import sys


hostName = ""
serverPort = 80
page = ""



if __name__ == "__main__":        
    
    page = sys.argv[1]
    interval = sys.argv[2]
    logFile = "/logger/"+page+".txt"

    if not os.path.exists(logFile):
        with open(logFile,"wt") as f:
            f.write("Status log of "+page+"\n")
    #page = os.environ['website']
    #interval = os.environ['interval']
    
    
    p = subprocess.Popen(["python3","./web.py",interval])
    with open("status","wt") as f:
        f.write("Program started")
    while True:
        statusCode = os.popen("curl -s -o /dev/null -w \"%{http_code}\" "+page).read().rstrip()
        now = datetime.datetime.now()
        
        if statusCode == '000':
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" not responding\n"
            web = "<a style=\"color:red;\">"+log+"</a>\n"
        
        elif statusCode[0] == '2':
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is Running\n"
            web = "<a style=\"color:green;\">"+log+"</a>\n"
        
        elif statusCode[0] == '3':
            redirectPage = os.popen("curl -s -o /dev/null -w \"%{redirect_url}\" "+page).read().rstrip()
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is Redirecting to "+redirectPage+"\n"
            web = "<a style=\"color:blue;\">"+log+"</a>\n"
        
        elif statusCode[0] == '4':
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is not allowing access\n"
            web = "<a style=\"color:red;\">"+log+"</a>\n"
                    
        elif statusCode[0] == '5':
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" have server issues\n"
            web = "<a style=\"color:red;\">"+log+"</a>\n"
        
        else:
            log = now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" returned unknown status code "+statusCode+"\n"
            web = "<a style=\"color:red;\">"+log+"</a>\n"
            
        with open("status","rt") as f:
            for line in f:
                web = web+line
        with open("status","wt") as f:
            f.write(web)
        with open(logFile,"at") as f:
            f.write(log)
        time.sleep(int(interval))   
        
    