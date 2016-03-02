import requests

headers ={
 'Accept':'*/*' ,
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With':'XMLHttpRequest',
'Referer':'http://www.zhihu.com',
'Accept-Language':'zh-CN',
 'Accept-Encoding':'gzip, deflate',
 'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)like Gecko',
'Host':'www.zhihu.com'
}
s =requests.session()
r = s.get('http://www.zhihu.com',headers =headers)

login_data ={
'_xsrf':'550f2554f9954c96ba55b53446ba74bd',
'email':'xxxx',
 'password': 'xxxx',
'remember_me':'false',
# 'captcha':captcha
}
s.post('http://www.zhihu.com/login/email', data=login_data, headers=headers)
r =s.get('http://www.zhihu.com')
print(r.text)
