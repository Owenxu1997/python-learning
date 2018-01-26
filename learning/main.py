import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


#download_web_image("")
"""
a = open('sample.txt', 'w')
a.write('writing something with my new python program\n')
a.write('this is awesome!')
a.close()

ar = open('sample.txt','r')
text = ar.read()
print(text)
ar.close()
"""

#downloading files from the web
from urllib import request

goog_url='https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1514209617&period2=1516888017&interval=1d&events=history&crumb=/ZWv7ayFvAS'

def download_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split()
    dest_url = r'goog_url'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()
