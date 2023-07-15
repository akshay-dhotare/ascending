# a='hello akshay'
# print(a)

# print('hello akshay!')

# a= 'hello akshay!'
# print(a,type(a),id(a))

# a=10
# b=10.20
# c='akshay'
# print(a,b,c,type(a),type(b),type(c),id(a),id(b),id(c))

# a=input('enter your first name :')
# b=input('enter your last name:')
# print('first name=',a,'last name=',b)


# wap area of square with value 6

# a=int(input('enter the value='))
# b=a*a
# print('area of square=',b)


# wap area of rectangular with l=10, w=20.2

# a=eval(input('enter the length='))
# b=eval(input('enter the width='))
# c=(a*b)
# print('are of rectangular=',c)


#wap area of circle with r=10

# a=eval(input('enter the radius='))
# b=eval(input('enter the pi='))
# c=(a*a*b)
# print('area of circle=',c)

# wap to find the square of 5 and 5.5

# a=int(input('enter the value='))
# b=(a*a)
# print('square of 5=',b)

# a=float(input('enter the value='))
# b=(a*a)
# print('square of 5.5=',b)

# wap to find cube of 8 and 9.8

# a=int(input('enter the value='))
# b=(a*a*a)
# print('cube of 8=',b)

# a=float(input('enter the value='))
# b=(a*a*a)
# print('cube of 8.8=',b)

# wap to find addition of  (45 + 45),(45 + 45.5)

# a=int(input('enter the first number='))
# b=int(input('enter the second number='))
# c=(a+b)
# print('the addition of 45 and 45 =', c)

# a=eval(input('enter the first number='))
# b=eval(input('enter the second number='))
# c=(a+b)
# print('the addition of 45 and 45.8 =', c)


# wap to find substractiion of (45-10) and (45.8-9)

# a=eval(input('enter the first number='))
# b=eval(input('enter the second number='))
# c=(a-b)
# print('the substraction of 45 and 10 =', c)


# a=eval(input('enter the first number='))
# b=eval(input('enter the second number='))
# c=(a-b)
# print('the substraction of 45.8 and 9 =', c)


# wap to find division of (90/9) and (66.6/3)

# a=eval(input('enter the first number='))
# b=eval(input('enter the second number='))
# c=(a/b)
# print('the division of 90 and 9 =', c)


# a=eval(input('enter the first number='))
# b=eval(input('enter the second number='))
# c=(a/b)
# print('the division of 66.6 and 6 =', c)
# **************************************************************************************************************************************

# a=True
# print(a,type(a),id(a))

# b=False
# print(b,type(b),id(b))


# a=12
# b=23
# c=(a<b)
# d=(a>b)
# print(c,d)


# a=True
# b=False
# c=True
# d=False
# e=(a+c)
# f=(a+b)
# g=(b+d)
# h=(b+c)
# print(e,f,g,h,type(e),type(f),type(g),type(h), type(a),type(b),type(c),type(d))

#*********************************************************************************************************************************

# import('keywords')
# print(keyword.kwlist)
#******************************************************************************************************************************

# complex data type

# a=10+20.7j
# print(a,type(a),id(a))

# a=22.2+22.8j
# print(a,type(a),id(a))

#********************************************************************************************************************************

# string data type 

# a='instagram'
# print(a,type(a),id(a))

# s='facebook'
# # print(s[6])
# # print(s[2:6])
# # print(s[2:8])
# # print(s[-1])

# s='instagram'
# print(s[5:])
# print(s[:])
# print(s[2:6:1])
# print(s[-2:-8:-2])
# print(s[-1:-9:-3])
# print(s[-1: :-4])
# print(s[ : :-2])
#************************************************************************************************************************************

#list data type
# l=[1,2,3,4,5,6,7,8]
#use append 
# l.append(10)
# print(l)
# l.append(20)
# print(l)
# l.append(-9)
# print(l)

# use insert
# l.insert(3,-9)
# print(l)
# l.insert(6,89)
# print(l)

#use slice
# print(l[2:6:2])
# print(l[-1:-6:-2])


#use pop
# l.pop(4)
# print(l)
# l.pop(7)
# print(l)

#use remove
# l.remove(8)
# print(l)
# l.remove(5)
# print(l)
#*****************************************************************************************************************************


#tuple data type
# t=(10,20,30,40,50,60)
# print(t,type(t),id(t))
# print(t[2])
# print(t[1:6:2])
# print(t[-1:-5:-1])

#********************************************************************************************************************************

#set data type

# s=set('akshay')
# print(s,type(s),id(s))
# s.add('mahesh')
# print(s)
# s.add('shobha')
# print(s)

# s.remove('shobha')
# print(s)
# s.remove('mahesh')
# print(s)

# for loop
# s={1,2,3,4,5,6,7,8,9}
# for i in s:
#     print(i)

# s={'akshay','mahesh','shobha','pandurang'}
# for i in s :
#     print(i)
#**************************************************************************************************************************

# frozenset
# a=frozenset('akshay')
# print(a,type(a),id(a))
#***********************************************************************************************************************

# range data type

# r=range(10)
# for i in r :
#     print(i)

# r=range(1,10)
# for i in r :
#     print(i)


# r=range(1,10,2)
# for i in r :
#     print(i)
#************************************************************************************************************************

# dict data type
# a={1:2,3:4,5:6}
# print(a,type(a),id(a))

# movie_dict={}
# movie_dict['don']=('sk','pc')
# movie_dict['radhe']=('sk','ss')
# movie_dict['dil']=('ak','mk')
# print(movie_dict)

# print keys only
# print(movie_dict['don'])
# print(movie_dict['radhe'])
# print(movie_dict.keys())


#print values only
# print(movie_dict.values())


# print key value pair
# print(movie_dict.items())

# for i in movie_dict.keys() :
#     print(i)


# for i in movie_dict.values() :
#     print(i)

# for i in movie_dict.items() :
#     print(i)

# for i,j in movie_dict.items() :
#     print(i,'=',j)

# movie_dict['don']=('sp','so')
# print(movie_dict)

#*********************************************************************************************************************************

# operators 
# 1 = arithmatic

# a=(4**2)
# print(a)

# a=(5**20)
# print(a)

# a=(9+8)
# print(a)

# a=(10-7)
# print(a)

# a=(10/2)
# print(a)

# a=(10//2)
# print(a)

# a=('akshay'+'mahesh')
# print(a)

# a=('akshay'*3)
# print(a)


# modulo operator(%) retruns reminder

# a=(47%2)
# print(a)  

# r= (47%2)
# if r == 0 :
#     print( ' the number is even')
# else :
#     print('the number is odd')


# a=23
# b=24
# c=(a<b)
# if c == True :
#     print('this is right')
# else:
#     print('this is wrong')

# a=45
# b=47
# c=(a>b)
# if c== False:
#     print('this is wrong')
# else:
#     print('this is right')

#********************************************************************************************************************


# logical operator
# 1= and operator
# a=True
# b=False
# c=a and b
# print(c)

# 2= or operator
# a= True
# b=False
# c=a or b
# print(c)

# 3 = not operator

# a=True
# b=False
# c= not(b) and (a)
# print(c)
######################################################################################################################################

# realatinonal operator 

# a=(10==10)
# print(a)

# b=(10==10.5)
# print(b)


# a=('facebook'!='whatsapp')
# print(a)

# b=('facebook'!='instagram')
# print(b)


# jay='18'
# viru='19'
#print('jay'=='viru')
# print('jay'>'viru')
# print('jay'<'viru')
# print('jay'<='viru')
# print('jay'>='viru')
# print('jay'!='viru')


# l=[24,30,45,57,-34,89,100,478,598,-49,59]
# for i in l:
    # if (i>20) and (i<100):
    #     print(i)
        # if (i>10) and (i%2==1):
        #     print(i)
        # if (i>10 and i<500 and i%2==1):
        #     print(i)
        # if (i>10 and i<500 and i%2==0):
        #     print(i)

#********************************************************************************************************************************


# composite assignment

# a=10
# a+=5
# print(a)

# a=20
# a+=25
# print(a)

# a=20
# a-=5
# print(a)

# a=50
# a-=10
# print(a)

# a=20
# a*=5
# # print(a)

# a=5
# a*=10
# print(a)

# a=10
# a/=2
# print(a)

# a=10
# a//=2
# print(a)

# a=10
# a**=2
# print(a)
#***********************************************************************************************************************************

# special operator
# 1) in

# a='instagram'
# b='i'
# print(b in a)
# c='g'
# print(c in a)
# d='R'
# print(d in a)
# e='M'
# print(e in a)


# 2) is 

# a=20
# b=20
# print(a is b)

# a=20
# b=20.5
# print(a is b)

#******************************************************************************************************************************

# flow control statement 
# 1) conditional statement - if , if-else ,if-elif-else

# age='18'
# if ('age'>'17'):
#     print('you are eligible') 

# age ='21'
# if 'age'>'20':
#     print('you are perfect')


# age=10
# if age > 20:
#    print('yes')          
# else:
#    print('no')



# a=18
# if a > 20:
#     print('yes')
# else:
#     print('no')


# a=eval(input('enter the marks='))
# if a > 80 and a < 90 :
#     print('grade a')
# elif a > 70 and a < 80 :
#     print('grade b')
# elif a > 60 and a < 70 :
#     print('grade c')
# else:
#     print('average')


# 3)iterative statemaent 

# for i in 'don':
#     print(10)
#     for j in 'van':
#         print(12)

# print(i)


# for i in 'me':
#     print(9)
#     for j in 'you':
#         print(8)

# print(i)


# i=1
# while i < 11:
#     print(i)
#     i+=1
# print(i)

# i=10
# while i < 30:
#     print(i)
#     i+=2

# print(i)


# transfer statement 
# 1) break 

# for i in 'instagram':
#     print(i)
#     if i=='a':
#         break

# for i in 'akshay':
#     print(i)
#     if i=='s':
#         break

# i=10
# while i < 50:
#     print(i)
#     i+=2
#     if i==42:
#         break

# while True:
#     print('python is simple')
#     choice=input('do you want to continue[y/n]:')
#     if choice=='n':
#         break


#3) continue
  

# l=[23,-45,10,5,-8,67,478,-98,55,28]
# l_new=[]

# for i in l:
#     if i< 0:
#         print(i)
#         continue
#     else:
#         num=i*-1
#         l_new.append(num)
    
#**************************************************************************************************************************

# input function

# g='6+7'
# h=eval(g)
# print(g)

#.format method 

# name = 'jay'
# roll=2
# marks=78
# print("student name is {n},roll no {r} and marks{m}".format(n=name,r=roll,m=marks))


# f " "
# a= 10
# b=20
# print(f"addtion of {a} and {b} is {a+b}")



















    














