# 判斷式
#x=input("請輸入數字: ") #取得字串形式的使用者訊息
#x=int(x) #將字串型態轉換成數字型態
#if x>200 :
#    print("大於 200")
#elif x>100 :
#    print("大於 100,小於等於 200")
#else:
#    print("小於等於100")
#四則運算
s1=int(input("請輸入第一個數字: "))
s2=int(input("請輸入第二個數字: "))
op=input("請輸入運算: +, -, *, /")
if op=="+":
    print(s1+s2)
elif op=="-":
    print(s1-s2)
elif op=="*":
    print(s1*s2)
elif op=="/":
    print(s1/s2)
else:
    print("不知支援此運算")
