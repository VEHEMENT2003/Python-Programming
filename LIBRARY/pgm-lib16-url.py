# wrking with browser
import urllib.request
import webbrowser
weburl=urllib.request.urlopen('http://www.VRUSHABH JADKAR.com/')
html=weburl.read()
data=weburl.getcode()
url=weburl.geturl()
hd=weburl.headers
inf=weburl.info()
print("the url is",url)
print("http staus code is",data)
print("headers returned\n",hd)
print("info returned\n",inf)
print("now opening",url)
webbrowser.open_new(url)
