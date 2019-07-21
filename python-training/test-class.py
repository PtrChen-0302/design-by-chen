#定義類別,與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO,有兩格屬性 supportedScrs　和　read
class IO:
    supportedSrcs=["console","file"]   #supportedSrcs支援的資料
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read From", src )
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")