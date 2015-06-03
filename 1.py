import urllib
import re

for a in range(1,5):

	url = "http://tieba.baidu.com/p/3785980987?pn=" +'%s' %a

	s = urllib.urlopen(url).read()


	def getimg(s1):
		reg = r'src="(.+[.jpg])" pic_ext'
		imgre = re.compile(reg)
		imgall = re.findall(reg,s1)
		x = 0
		for imgurl in imgall:
			urllib.urlretrieve(imgurl,'D:/%s.jpg' % x)
			x = x + 1 

	a = a + 1
getimg(s)

