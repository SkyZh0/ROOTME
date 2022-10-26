import socket
import math as ma

TCP_IP = 'challenge01.root-me.org'
TCP_PORT = 52018
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


data = s.recv(BUFFER_SIZE)


data = data.decode("UTF-8")
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
li[3].remove('=')
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




def solver(a,b,c,d):
    c = c - d
    delta = b**2 - (4*a*c)
    if delta > 0:
        return("x1: " + str((-b + ma.sqrt(delta))/2*a) + " ; x2: " + str((-b - ma.sqrt(delta))/2*a))
    elif delta == 0:
        return ("x: " + str((-b)/(2*a)))
    elif delta < 0:
        return "Not possible"

n = s.send(solver(a,b,c,d).encode("UTF-8"))
if n != len(solver(a,b,c,d)):
    print("Erreur")
else:
    print("envoi ok")