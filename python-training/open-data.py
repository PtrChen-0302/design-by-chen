#網路連線
#串接,攝取公開資料
import urllib.request as request
src="http://www.ntu.edu.tw"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") #取得台灣大學網站的原始碼(HTML,CSS,JS )
import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as reponse:
    data=json.load(reponse)  #利用json模組,處理json資料格式
print(data) 
#將公司名稱列表出來
clist=data["result"]["results"]
#將資料存入"data.txt" 
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")

