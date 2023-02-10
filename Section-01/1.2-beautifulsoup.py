from urllib.request import urlopen  # 查找python中的request模块，导入urllib函数
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')  # 利用urlopen来读取远程对象的内容

# bs = BeautifulSoup(html.read(),'html.parser') #将获取到的远程内容，利用parser解析器进行解析，并存储在bs中
# print(bs.h1) #显示网页结构中h1的内容
# print(bs.div)

# bs = BeautifulSoup(html.read(), 'lxml') # lxml 为解析器，与html.parser的作用类似，其优点在于解析杂乱的信息，但其需要独立安装
# print(bs.h1)
# print(bs.div)

bs = BeautifulSoup(html.read(), 'html5lib') # html5lib 为解析器，其解析杂乱信息的程度比lxml性能更高，但耗时较长。
print(bs.h1)
print(bs.div)

# 网页结构如下所示。
#    html --->   <html><head>...</head> <body> ...</body></html>
#    ----head --->  <head><title>A Useful Page</title> </head>
#        ----title  ---> <title>A Useful Page</title>
#    ----body --->  <body><h1>An Int.....</h1> <div>Lorem ip....</div></body>
#        ----h1  ---> <h1>An Interesting Title</h1>
#        ----div  ---> <div>Lorem Ipsum dolor</div>
