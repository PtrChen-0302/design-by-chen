#參數的預設資料
# def power(base,exp=0):
#     print(base**exp)
# power(3,2)
# power(4)
#使用參數名稱對應
# def divide(n1,n2):
#     print(n1/n2)
# divide(3,6)
# divide(n1=6,n2=3)
#無限/不訂 參數資料
def avg(*ns):
    sum=0
    for x in ns:
        sum+=x
    print(sum/len(ns))
avg(7,5,6)