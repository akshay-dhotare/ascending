class gp():
    def m1(self):
        print('this is grandparent m1 method ')

class p1(gp):
    def m2(self):
        print('this is parent1 m2 method ')

class p2(gp):
    def m3(self):
        print('this is parent2 m3 method ')

class p3(gp):
    def m4(self):
        print('this is parent3 m4 method ')

class p4(gp):
    def m5(self):
        print('this is parent4 m5 method ')

class w1(p1):
    def m6(self):
        print('this is wife1 of parent1 m6 method')

class c1(w1,p1):
    def m7(self):
        print('this is child1 of p1 and w1 m7 method')

class c2(p3):
    def m8(self):
        print('this is child2 of p3 m8 method')

class c3(p3):
    def m9(self):
        print('this is child3 of p3 m9 method')

class c4(p3,gp):
    def m10(self):
        print('this is child4 of gp and p3 m10 method')

class c5(p4):
    def m11(self):
        print('this is child5 of parent 4 m11 method')


jay=c5()
jay.m11()
jay.m5()

viru=c4()
viru.m10()
viru.m4()
viru.m1()

tom=c3()
tom.m9()
tom.m4()

mom=c2()
mom.m8()
mom.m4()

akshay=c1()
akshay.m7()
akshay.m6()
akshay.m2()
