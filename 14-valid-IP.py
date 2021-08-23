# 14. Write a program to valid and IP address. 

import socket 
addr = input("Enter your IP address: ")

try: 
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")