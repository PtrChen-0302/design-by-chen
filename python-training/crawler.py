# 抓取ptt電影版的網頁原始碼(HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#建立一個Request 物件,附加 Request Header 的資訊
request=req.Request(url, headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)
# 解析原始碼 ,取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser") #讓 beautifulsoup 協助我們解析 HTML 格式文件
titles= root.find_all("div",class_="title") #尋找所有class="title" 的 div 標籤
for  title in titles:
    if title.a != None: #如果標題包含 a 標籤(沒有被刪除), 印出來
        print(title.a.string)
        

