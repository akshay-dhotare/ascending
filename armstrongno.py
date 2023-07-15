# num=407
# s=str(num)
# n=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**n
# if sum==num:
#     print('armstrong')
# else:
#     print('no')


num=303
s=str(num)
n=len(s)
sum=0
for i in s:
    sum=sum+int(i)**n
if sum==num:
    print('armstrong')
else:
    print('no')