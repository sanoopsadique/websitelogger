
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os, datetime
import subprocess
#import os 
import sys


hostName = ""
serverPort = 80
page = ""


if __name__ == "__main__":        
    
    page = sys.argv[1]
    interval = sys.argv[2]
    
    #page = os.environ['website']
    #interval = os.environ['interval']
    
    
    p = subprocess.Popen(["python3","/weblogger/web.py",interval])
    with open("status","wt") as f:
        f.write("Program started")
    while True:
        statusCode = os.popen("curl -s -o /dev/null -w \"%{http_code}\" "+page).read().rstrip()
        now = datetime.datetime.now()
        
        if statusCode == '000':
            msg = "<a style=\"color:red;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" not responding</a>\n"
        
        elif statusCode[0] == '2':
            msg = "<a style=\"color:green;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is Running</a>\n"
        
        elif statusCode[0] == '3':
            redirectPage = os.popen("curl -s -o /dev/null -w \"%{redirect_url}\" "+page).read().rstrip()
            msg = "<a style=\"color:blue;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is Redirecting to "+redirectPage+"</a>\n"
        
        elif statusCode[0] == '4':
            msg = "<a style=\"color:red;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is not allowing access</a>\n"
        
        elif statusCode[0] == '5':
            msg = "<a style=\"color:red;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" is having server issues</a>\n"
        
        else:
            msg = "<a style=\"color:red;\">"+now.strftime("%y-%m-%d-%H:%M:%S")+" - "+page+" returned unknown status code "+statusCode+"</a>\n"
            
        with open("status","rt") as f:
            for line in f:
                msg = msg+line
        with open("status","wt") as f:
            f.write(msg)
        time.sleep(int(interval))   
        
    