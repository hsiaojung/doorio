import urllib.request
import urllib.parse
 
  
url = 'http://www.wisoft.com.tw/reedot/checknow.jsp?id=ooooo&io=0&gate=1'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
