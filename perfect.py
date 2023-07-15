use=eval(input('enter the number:'))
sum=0
for i in range(1,use):
    if use%i==0:
        sum=sum+i
if sum==use:
    print('given number is perfect')
else:
    print('given number is not perfect')
        


