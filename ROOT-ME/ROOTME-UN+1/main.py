from ast import expr
import requests
import urllib

challenge = 'http://challenge01.root-me.org/programmation/ch1/'

def code_of_site(url):
    weburl = urllib.request.urlopen(url)
    code = weburl.read()
    return code

ocode = code_of_site(challenge).decode("UTF-8")
code = ''
for i in range(214,len(ocode)-170):
    code = code + ocode[i]
code = code.split()


expression = "("+ str(code[1]) + code[2] + "U)" + " " + code[5] + " " + '(n' + '*' + "(" + str(code[9]) +")" +")"

U = int(code[14])

tempn = code[19]
n = ''
for i in tempn:
    if i.isdigit():
        n = n + i
        
n = int(n)

def func(u,n):
    i1 = int(code[1])
    i2 = int(code[9])
    if code[2] == '+' and code[5] == '+':
        return (i1+u)+(n*i2)
    elif code[2] == '-' and code[5] == '+':
        return (i1-u)+(n*i2)
    elif code[2] == '+' and code[5] == '-':
        return (i1+u)-(n*i2)
    elif code[2] == '-' and code[5] == '-':
        return (i1-u)-(n*i2)

for i in range(1,n):
    U = func(U,i)


result = U

URL = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="
param = str(result)
URL = URL + param
output = requests.get(url = URL, params = param)
output = output.text

print(output)



"""
OTHER SOLUTION

import requests    
from bs4 import BeautifulSoup
     
url="http://challenge01.root-me.org/programmation/ch1/"
flagurl=""
ans=b""
while b"Congratz!" not in ans:
    page=requests.get(url)
    cook=page.cookies
    soup=BeautifulSoup(page.content,"html.parser")
    text=(soup.text).split('\n') #all text in the page
    r1=text[0].split(' ') #row1 or the expression
    x=int(r1[3]) #x and y  are as in Un+1 = [ x + Un ] + [ n * y ]
    y=int(r1[11])
    a=int((text[1].split(' ')[2].replace('\n','')))  #first term
    n=int((text[2].split(' ')[3].replace('U','').replace('You',''))) #last term to calculate
    flagurl=((text[2].split(' ')[18]).replace('...)','')) #url where result has to send
    res=(n*x+a+y*(n-1)*n//2)
    print(res)
    ans=(requests.get(flagurl+str(res),cookies=cook).content)
    print(ans)


"""