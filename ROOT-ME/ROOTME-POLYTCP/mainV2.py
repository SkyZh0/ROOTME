import socket
from telnetlib import Telnet
import math as ma

#SOLVER FUNC

def solver(a,b,c,d):
    c = c - d
    delta = b**2 - (4*a*c)
    if delta > 0:
        x1 = round(
            ((-b + ma.sqrt(delta))/(2*a)),3
        )
        x2 = round(
            ((-b - ma.sqrt(delta))/(2*a)),3
        )
        return("x1: " + str(x1) + " ; x2: " + str(x2))
    elif delta == 0:
        x = round(
            (-b)/(2*a), 3
        )
        return ("x: " + str(x))
    elif delta < 0:
        return "Not possible"
    
    
    
#TCP CONNX

TCP_IP = 'challenge01.root-me.org'
TCP_PORT = 52018
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

t = Telnet()
t.sock = sock

for i in range(25):
    data = (t.read_until("?>".encode("ascii")))
    data = data.decode("UTF-8")
    print(data)
    data = data.split('[>]')
    data = data[len(data)-1]
    data = [data[i] for i in range(10,len(data)-1)]

    nums = ''
    for i in data:
        if i.isdigit() or i == '+' or i == '-' or i == '=':
            nums = nums + i

    nums2 = ''

    for i in nums:
        if i != '²' and i != '¹':
            nums2 = nums2 + i

    li = [[],[],[],[],[],[]]
    count = 0
    for i in nums2:
        if i != '+' and i != '-' and i != '=':
            li[count].append(i)
        else:
            count += 1
            li[count].append(i)
    li.remove([])
    try:
        li[3].remove('=')
    except:
        pass
    li.remove([])

    a,b,c,d = '','','',''
    for i in li[0]:
        a = a+i
    for i in li[1]:
        b = b+i
    for i in li[2]:
        c = c+i
    for i in li[3]:
        d = d+i
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    solution = solver(a,b,c,d)
    print(solution)
    t.write(solution.encode("UTF-8") + b"\n")
    
        

print(t.read_all())
t.close()