#-*- coding:utf-8 -*- 
import urllib
import re
import string



url = "http://www.douban.com/group/haixiuzu/"
s = urllib.urlopen(url).read()
#unicodePage = unicodePage.decode("gbk")



def gettext(s1):
    
    reg = r'title=".+" class='
    
    textre = re.compile(reg)
    textall = re.findall(reg,s1)
    t = ('\n').join(textall)
    print t
    f = open('D:/text.txt','w')
    f.write(t+'\n')
    f.close()
    #print textall
    #f = open('D:/text.txt','w')
    #f.write(textall).decode("gbk")
    #f.close()

       
gettext(s)
