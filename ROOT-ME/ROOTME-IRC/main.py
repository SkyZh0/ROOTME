from irc_class import *
import os
import random
import math as ma


## IRC Config
server = "irc.root-me.org" # Provide a valid server IP/Hostname
port = 6667
channel = "#root-me_challenge"
botnick = "challenge"
botnickpass = ""
botpass = ""
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
    if 'ping' in text:
      irc.send(channel,'pong')
    if 'execute' in text:
     irc.send("Candy", "!ep1")
    if "Candy" in text:
      text = str(text)
      result = []
      for i in text:
        if i.isdigit() or i == '/':
          result.append(i)
      print(result)
      i1 = ''
      i2 = ''
      bool = False
      for i in text:
        if i.isdigit() and not(bool):
          i1 = i1 + i
        if i == '/':
          bool = True
        if i.isdigit() and bool:
          i2 = i2 + i
      i1,i2 = i1.split(),i2.split()
      if len(result) < 10:
        i1 = int(i1[0])
        i2 = int(i2[0])
        print('\n',i1,'\n',i2, type(i1), type(i2))
        i3 = round(ma.sqrt(i1)*i2,2)
        irc.send("Candy","!ep1 -rep " + str(i3))
      