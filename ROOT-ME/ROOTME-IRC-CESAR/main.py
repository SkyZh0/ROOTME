from irc_class import *
import os
import random
import math as ma
import base64
import time


def rot_encode(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


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
     irc.send("Candy", "!ep3")
    if "Candy" in text:
      text = str(text)
      result = [text[i] for i in range(text.index(':',10), len(text)-1)]
      result = [result[i] for i in range(1,len(result)-1)]
      stresult = ''
      for i in result:          
        stresult = stresult + i
      if len(stresult) < 50:
        print(stresult, rot_encode(-13)(stresult))
        irc.send("Candy", "!ep3 -rep " + rot_encode(-13)(stresult))
      