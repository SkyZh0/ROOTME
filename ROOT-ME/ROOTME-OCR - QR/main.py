#By SkyZh0 with the help of mouthon#2032

from PIL import Image
import numpy as np
import requests
from bs4 import BeautifulSoup
import base64
import os


URL = "http://challenge01.root-me.org/programmation/ch7/"
s = requests.Session()
code = (s.get(url=URL)).text


SC = ''
htmldata = code
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    SC = SC + item['src']
    
SC = (SC.split(','))[1]

ddata = base64.b64decode(SC)
Ifile = open('SC.png', 'wb')
Ifile.write(ddata)
Ifile.close()


#im.paste(foreground, (0, 0), foreground)
#im.save('QRTest.png')
#pour info la methode paste marche aussi

IM = Image.open("AP.jpg")
SC = Image.open("SC.png")

SC.convert("RGB")
IM.convert("RGB")

Idata = np.array(IM)
data = np.array(SC)

for i in data:
    for j in i:
        if j[0] > 20 and j[1] > 20 and j[2] > 20:
            j[0],j[1],j[2] = 60,180,120

for i in range(len(data)-1):
    for j in range(len(data[i])-1):
        if data[i][j][0] != 60 and data[i][j][1] != 180 and data[i][j][2] != 120:
            Idata[i][j][0], Idata[i][j][1], Idata[i][j][2] = 0,0,0

final = Image.fromarray(Idata)
final.save('final.jpg')


result = ''
apiURL = 'http://api.qrserver.com/v1/read-qr-code/'
with open('final.jpg','rb') as img:
    name_img= os.path.basename('final.jpg')
    files= {'file': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
    with requests.Session() as q:
        r = q.post(apiURL,files=files)
        result = result + r.text

result = (result.split(',')[2].split(' ')[3])
result = result[1:len(result)-1]


result_data = {"metu": result}
resp = s.post(url=URL, data=result_data)


print(f'FINAL RESPONSE with code {result}: ', resp.text[0:300])
