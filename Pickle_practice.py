import urllib.request
import pickle

content=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.load(content)

print(data)

for line in data:
    print("".join([k * v for k, v in line]))
