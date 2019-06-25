import urllib.request
import re

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
num='12345'
content=urllib.request.urlopen(url%num).read().decode('utf-8')

for n in range(1,400):
    pos=content.find('and the next nothing is')
    if bool(pos+1) :
        content=content[pos:]
        lst=content.split(' ')
        for ele in lst[:7]:
            if ele.isdigit():
                num=ele
                content=urllib.request.urlopen(url%num).read().decode('utf-8')
                print(content)
                print(n)
    elif content=="Yes. Divide by two and keep going.":
        num=int(num)/2
        content=urllib.request.urlopen(url%num).read().decode('utf-8')
        print(content)
        print(n)




