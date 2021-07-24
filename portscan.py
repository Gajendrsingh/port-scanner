from datetime import datetime
import pyfiglet 
import socket
import sys 
import socket
ascii_banner = pyfiglet.figlet_format("illuminati world secret socitey port scan tool made by kelvin") 

print(ascii_banner) 
target = input("enter ip adress")

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
     print("inavid host")



print("_" * 50)
print("target: "+ target)
print("target scan at:" + str(datetime.now()))
print("_" * 50)

try:
     for port in range(1,65535):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         
         socket.setdefaulttimeout(1)

         result = s.connect_ex((target,port))

         if result  ==0:
             print("port {} is open".format(port))
         s.close()




