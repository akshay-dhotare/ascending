# def add():
#     fd=open('data','w')
#     a=eval(input('enter the 1st no:'))
#     b=eval(input('enter the 2nd no:'))
#     c=(a+b)
#     print(c)
#     s=f"addition of {a} and {b} is ={c}"
#     fd.write(str(s))
#     fd.close()

# add()

# def division():
#     fd=open('data','a')
#     a=eval(input('enter the 1st no:'))
#     b=eval(input('enter the 2nd no:'))
#     d=(a//b)
#     print(d)
#     w=f" division of {a} and {b} is = {d}"
#     fd.write(str(w))
#     fd.close()

# division()

# def operation():
#     fd=open('info.txt','w')
#     a=eval(input('enter the 1st no:'))
#     b=eval(input('enter the 2nd no:'))
#     c=(a-b)
#     d=(a*b)
#     print(c)
#     print(d)
#     w=(f"substraction of {a} and {b} is = {c} and multiplication of {a} and {b} is = {d}")
#     fd.write(str(w))
#     fd.close()

# operation()

# def area():
#     fd=open('info.txt','a')
#     a=eval(input('enter the 1st no:'))
#     b=eval(input('enter the 2nd no:'))
#     c=(a*b)
#     d=(a*a)
#     print(c)
#     print(d)
#     w=(f"area of reactangular is {c} and area of sqaure is {d} ")
#     fd.write(str(w))
#     fd.close()

# area()


def area():
    fd=open('info.txt','a')
    a=eval(input('enter the 1st no:'))
    b=eval(input('enter the 2nd no:'))
    c=(a*b)
    d=(a*a)
    print(c)
    print(d)
    w=(f"area of reactangular is {c} and area of sqaure is {d} ")
    fd.writelines(list(w))
    fd.close()

area()






