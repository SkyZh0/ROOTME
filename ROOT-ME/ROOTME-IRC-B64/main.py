from irc_class import *
import os
import random
import math as ma
import base64


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
     irc.send("Candy", "!ep2")
    if "Candy" in text:
      text = str(text)
      result = [text[i] for i in range(text.index(':',10), len(text)-1)]
      result = [result[i] for i in range(1,len(result)-2)]
      stresult = ''
      for i in result:          
        stresult = stresult + i
      if len(stresult) < 50:
        message = str(stresult) + "=="
        message = base64.b64decode(message)
        message = message.decode("UTF-8")
        irc.send("Candy","!ep2 -rep "+ message)
      