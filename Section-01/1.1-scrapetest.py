from urllib.request import urlopen #查找python中的request模块，导入urllib函数

html = urlopen('http://www.pythonscraping.com/pages/page1.html') #利用urlopen来读取远程对象的内容
print(html.read()) #展示远程对象的内容，但并没有结构，显得较为杂乱