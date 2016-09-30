import urllib2
import ctypes
from HTMLParser import HTMLParser


response = urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html')
html = response.read()

class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        if tag == "a":
           for name, value in attrs:
               if name == "href":
                   if value.endswith("jpg"):
                       self.output=value

parser = MyHTMLParser()
parser.feed(html)
imgurl='http://apod.nasa.gov/apod/'+parser.output
print imgurl


img = urllib2.urlopen(imgurl)
localFile = open('desktop.jpg', 'wb')
localFile.write(img.read())
localFile.close()