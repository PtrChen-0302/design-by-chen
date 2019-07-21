#break 簡易示範
#n=0
#while n<5:
#    if n==3:
#        break
#    print(n) #印出巡迴中的 n
#    n+=1
#print("最後的n: ",n) #印出最後的 n
#continue 簡易示範
#n=0
# for x in [1,2,3,4]:
#     if x%2==0: #x 是偶數
#         continue
#     print(x)
#     n+=1
# print("最後的 n :",n)


#else 簡易示範
# sum=0
# for x in range(11):
#     sum+=x
# else:
#     print(sum) #印出0+1+2+3...+10 的結果

#綜合範例 找出平方根
#輸入9 得到平方根 3
#輸入11得到平方[沒有]

# x=int(input("輸入一個整數: "))
# for i in range(x): #從0 ~ n-1
#      if i*i==x:
#          print("整數平方根",i)
#          break #用break 強制停止迴圈時,不會執行else
# else:
#     print("沒有整數根")

# for x in range(1,10):
#     if x == 5:
#         break
#     print(x,end="")