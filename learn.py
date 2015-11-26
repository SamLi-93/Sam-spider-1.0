import urllib
import re

url = "http://tieba.baidu.com/p/2962968913"

source = urllib.urlopen(url)
html = source.read()

def getimg(img):
    reg = r'src="(.+[.jpg])" pic_ext'
    imgre = re.compile(reg)  
    
    l = re.findall(reg, img)
    x = 0
    for imgurl in l:  
        # urllib.urlretrieve(imgurl,'D:/%s.jpg' % x)  
        urllib.urlretrieve(imgurl,'.jpg' %x)
        x = x + 1      



getimg(html)

