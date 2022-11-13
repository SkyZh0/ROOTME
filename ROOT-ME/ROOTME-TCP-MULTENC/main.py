from email.mime import base

import socket 
from telnetlib import Telnet
import base64
from nltk.corpus import words
import difflib


#dict
MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


#decoder
def morse(st):
    result = []
    st = st.split('/')
    for code in st:
        for dic in MORSE_CODE_DICT.items():
            if code == dic[1]:
                result.append(dic[0])
    return ''.join(result)

def decode(st):
    result = []
    try:
        result.append(base64.b64decode(st).decode('UTF-8'))
    except:
        pass
    try:
     result.append(bytes.fromhex(st).decode('UTF-8'))
    except:
        pass
    try:
        result.append(base64.b85decode(st).decode('UTF-8'))
    except:
        pass
    try:
        result.append(morse(st))
    except:
        pass
    try:
        result.append(base64.b32decode(st).decode('UTF-8'))
    except:
        pass
    return result



#finder
def finder(st):
    li = decode(st)
    print(li)
    for wd in li:
        if difflib.get_close_matches(wd.lower(), words.words()) != []:
            return wd




#TCP CONNX
TCP_IP = 'challenge01.root-me.org'
TCP_PORT = 52017
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

t = Telnet()
t.sock = sock


#main
for i in range(100):
    data = (t.read_until("?>".encode("ascii")))
    data = data.decode("UTF-8")
    print(data)
    data = data.split('[>]')

    message = ''
    bool = False
    for i in data[len(data)-1]:
        if i == "'":
            bool = not(bool)
        if bool:
            message = message + i
    message = message.split("'")[1]
    
    t.write(finder(message).encode("UTF-8") + b"\n")
    
print(t.read_all())
t.close()
    




