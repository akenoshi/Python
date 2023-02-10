############################################################
#                                                          #
#                     block 1                              #
#                                                          #
############################################################

# from urllib.error import HTTPError  # 检查http程序是否正确运行
# from urllib.request import urlopen  # 查找python中的request模块，导入urllib函数
#
# try:
#     html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)  # 返回空值，中断程序，或者执行另一种方案
# else:
#     print(404)

############################################################
#                                                          #
#                     block 2                              #
#                                                          #
############################################################

# from urllib.request import urlopen # 查找python中的request模块，导入urllib函数
# from urllib.error import HTTPError # 检查http程序是否正确运行
# from urllib.error import URLError # 用来检查http的链接是否畅通可行，决定是否报错
#
# try:
#     html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
# except HTTPError as e:
#     print("The server returned an HTTP error")
# except URLError as e:
#     print("The server could not be found!") # 服务器不存在
# else:
#     print(html.read())


############################################################
#                                                          #
#                     block 3                              #
#                                                          #
############################################################

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url): #定义getTitle的处理方法
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)