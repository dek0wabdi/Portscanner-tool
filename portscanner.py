import sys
import socket
from datetime import datetime
#Then Define the target
if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax:python3 portscanner.py <IP>")
    sys.exit()
#Then add a banner
print("-" *50)
print("Scanning the target" + target)
print("Time started:" + str(datetime.now()))
print("-" * 50)
try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Returns an error indicator
        print("Checking port{}" .format(port))
        if result==0:
            print("Port {} is open") .format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting the program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connet to the server")
    sys.exit()
