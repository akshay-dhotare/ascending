# print('lets find addttion of two no')

# def addttion_of_two_no():
#     print('we are inside the function')
#     a=eval(input('enter the value:'))
#     b=eval(input('enter the value:'))
#     c=(a+b)
#     print(f"addtion of two no with {a}+{b}={c}")

# print(' we are calling function from outside')
# addttion_of_two_no()


# def reverse_string():
#     s='java'
#     print(s[ : :-1])

# reverse_string()


# def count_no_char():
#     s='python'
#     print(len(s))

# count_no_char()


# def index_no():
#     s='python'
#     print(s[3])

# index_no()

# def count():
#     s='rameshwaram'
#     c=0
#     for i in s:
#         c=c+1
#     print(c)

# count()

# def count():
#     s='rameshwarm'
#     c=0
#     for i in s:
#         if i=='a':
#             c=c+1
#     print(c)

# count()


print('we are in global space')
x=100
def outer_fun():
    print('we are in local scope of outer function')

    def inner_fun():
        print('we are in local scope of inner function')

        print('we are calling inner function from local scope of outer function')
        print('we are in super inner function')
        inner_fun()
        return inner_fun

print('we are calling outer function from global scope')
inner_fun=outer_fun()
print(type(inner_fun))



# print('we are calling inner function from global scope')
# inner_fun()

