import socket
from datetime import date, datetime
import calendar

def Client(ipAddress):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ipAddress,GetPort()))
    while(1):
        user_command = input("~/")
        while not user_command:
            user_command = input("~/")
        if user_command == "exit":
            s.sendall(b"exit\n")
            break
        s.sendall((user_command).encode())
        print(s.recv(1024).decode())
    s.close()    



def GetPort():
    day = calendar.day_name[date.today().weekday()]
    hash = 1
    for i in day :
        hash *= ord(i) 
    return (hash + datetime.now().minute) % 65535


print(GetPort())
Client("192.168.100.50")