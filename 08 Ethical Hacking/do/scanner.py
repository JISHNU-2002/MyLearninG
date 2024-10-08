import sys
import socket
from datetime import datetime

# define target
if len(sys.argv) == 2:
    # hostname to ipV4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print('invalid amount of arguments')
    print('Syntax : python3 scanner.py <ip>')

# python3 scanner.py <ip>

# add a pretty banner
print('-'*50)
print('Scanning target : '+target)
print('Time started : '+str(datetime.now()))
print('-'*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex(target.port)
        print('Checking port {}'.format(port))
        
        if result == 0:
            print('Port {} is open'.format(port))
        s.close()
        
except KeyboardInterrupt:
    print('Exiting program')
    sys.exit()
    
except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()
    
except socket.error:
    print('Could not connect to server')
    sys.exit()
        
