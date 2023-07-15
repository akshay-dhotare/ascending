# class AgeTooSmallError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# class AgeTooBigError(Exception):
#     def __init__(self,msg):
#         self.msg=msg


# age=eval(input('enter your age:'))
# if age<18:
#     raise AgeTooSmallError('your age is too small for RTO licence')
# elif age>65:
#     raise AgeTooBigError('your age is too Big for RTO licence')
# else:
#     print('welcome to pune RTO website. fill this form for licence.')


# class AgeTooSmallError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# class AgeTooBigError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# age=eval(input('enter your age:'))
# if age<18:
#     raise AgeTooSmallError('your age is too small for attending this boxing club')
# elif age>65:
#     raise AgeTooBigError('your age is too Big for attending this boxing club')
# else:
#     print('welcome to miketyson boxing club. enjoy your boxing journey with us.')



# class DebitAccountError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# class CreditAccountError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# money=eval(input('enter your amount:'))
# if money<1000:
#     raise DebitAccountError('your amount is too less for debit money..')
# elif money>10000:
#     raise CreditAccountError('your amount is too big for credit money at this time...')
# else:
#     print('welcome to the sbi bank transaction process...')

# class LessEyeIssueError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# class MoreEyeIssueError(Exception):
#     def __init__(self,msg):
#         self.msg=msg

# eyenumber=eval(input('enter your eye number:'))
# if eyenumber<2:
#     raise LessEyeIssueError('your eye is in good condition do not worry...')
# elif eyenumber>5:
#     raise MoreEyeIssueError('your eye is in bad condition you required eye therapy...')
# else:
#     print('your eye is stable. you have good vision...')
