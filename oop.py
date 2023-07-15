# # class home:
# #     def _init_(self,ml,m,c):
# #      self.material=ml 
# #      self.money=m 
# #      self.color=c 

# #     def get_details(self):
# #         print(f"for home material required is {self.material},money is {self.money} and color is {self.color}")


# # h1=home('cement',15000,'red')
# # h1.get_details()

# # h2=home('bricks',20000,'blue')
# # h2.get_details()

# class bike:
#     def __init__(self,cl,pr,mo):
#         self.color=cl
#         self.price=pr
#         self.model=mo

#     def get_details(self):
#         print(f"bike color is {self.color},price is {self.price} and model is {self.model}")

# b1=bike('red',15000,'two w')
# b1.get_details()

# b2=bike('pink', 20000, 'two w')
# b2.get_details()


# class laptop:
#     def _init_(self,cl,wn,ca):
#         self.color=cl
#         self.windows=wn
#         self.camera=ca

#     def get_details(self):
#         print(f"laptop color is {self.color},windows is {self.windows} and camera is {self.camera}")

# l1=laptop('red',11,'frontend')
# l1.get_details()

# l2=laptop('pink',12,'backend')
# l2.get_details()

class laptop:
    def __init__(self,cl,wn,ca):
        self.color=cl
        self.windows=wn
        self.camera=ca

    def get_details(self):
        print(f"laptop color is {self.color},windows is {self.windows} and camera is {self.camera}")

l1=laptop('red',11,'frontend')
l1.get_details()

l2=laptop('pink',12,'backend')
l2.get_details()