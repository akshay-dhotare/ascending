class test:
    def __init__(self):
        self.x=100

    
    def m1(cls):
        print(cls.x)


t=test()
t.m1()