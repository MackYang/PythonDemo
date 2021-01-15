#coding=utf-8
#这是一个爬某篇文章的示例
import requests
import sys
import bs4

if len(sys.argv) < 3:
    print("please enter the url, example: python3 test1.py http://xxx.xxx")
    sys.exit()
#某本书的url地址
url = sys.argv[2]
#生成的文件文件保存的位置
directory = sys.argv[1]

print('start spider...')
#基础url地址，用作地址拼接，自动爬取所有章节的小说
baseurl = "http://www.biquge.com.tw"
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
#获取书名
bookname = soup.select('#info > h1')[0].getText()
#解析html结构，dl下边有N个dd，dd中的a标签的href属性保存了对应章节的具体url地址
chapters = soup.select('#list > dl > dd')
print(len(chapters))
for chapter in chapters:
    atag = chapter.select('a')[0]
    chapter_url = atag.get('href')
    #拼接完整的url地址逐个去爬取数据
    full_url = baseurl + chapter_url
    article_res = requests.get(full_url)
    article_soup = bs4.BeautifulSoup(article_res.text, 'lxml')
    #查找小说内容的标签，小说内容存在id为content的div中
    article_content = article_soup.select('#content')[0]
    #查找小说的章节标题
    article_title = article_soup.select('.bookname > h1')[0]
    print('爬取:' + article_title.getText().encode('iso-8859-1').decode('gbk') + ' 的内容中...')
    #以\r\n为标示分割一篇文章，将一章的小说内容分割为一个列表
    lines = article_content.getText().split('\r\n')
    print('爬取章节完成，开始写入文件...')
    myfile = open(directory + "/" + bookname.encode('iso-8859-1').decode('gbk') + ".txt", 'a', encoding='iso-8859-1')
    myfile.write(article_title.getText() + '\n')
    for line in lines:
        myfile.write(line.strip() + '\n')
    myfile.write('\n\n\n')
    print('章节写入文件完毕!')
myfile.close()