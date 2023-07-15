db=[]
def dashboard():
    print('#'*90)
    print('\t\t welcome to the grocery object list')
    print('''     
                   MENU
                   1)add grocery object
                   2)display grocery
                   3)update grocery list
                   4)delete grocery object
                   5)search grocery       
                                           ''')


class grocery():
    def __init__(self,nm,pr,qu,ty):
        self.grocery_name=nm
        self.grocery_price=pr
        self.grocery_quantity=qu
        self.grocery_type=ty

    def add_grocery_object(self):
        nm=input('enter the name of grocery object:')
        pr=eval(input('enter the price of grocery|:'))
        qu=input('enter the quantity of grocery object:')
        ty=input('enter the type of grocery object:')

        g1=grocery(nm=nm,pr=pr,qu=qu,ty=ty)
        db.append(g1)
        print('grocery {g1.name} added sucessfully in database...')

    def display_grocery(self):
        print('-'*85)
        print("|{nm:^20}|{pr:^20}|{qu:^20}|{ty:^20}".format(nm='name',pr='price',qu='quantity',ty='type'))
        print('-'*85)
        for i in db:
            print("|{nm:^20}|{pr:^20}|{qu:^20}|{ty:^20}".format(nm=i.name,pr=i.price,qu=i.quantity,ty=i.type))
            print('-'*85)

    def search_grocery(self):
        g_price=eval(input('enter the price of the grocery object:'))
        for i in range(len(db)):
            if db[i].price==g_price:
                print('grocery object found in database')
                return i
        return-1

    def delete_grocery(self):
        i=dummy_obj.search_grocery()
        if i>=0:
            del db[i]
            print('grocery object deleted sucessfully from the list...')
        else:
            print('grocery price not found in the database...')

    def update_grocery(self):
        i=dummy_obj.search_grocery()
        if i>=0:
            nm=input('enter updated grocery object: ')
            pr=eval(input('enter updated grocery price:'))
            qu=input('enter updated quantity of the grocery object:')

            db[i].name=nm
            db[i].price=pr
            db[i].quantity=qu
            print('grocery list updated sucessfully...')
        else:
            print('grocery name not found in the db...')

    def price_grocery(self):
        g_price=eval(input('enter your price:'))
        print('-'*85)
        print("|{nm:^20}|{pr:^20}|{qu:^20}|{ty:^20}".format(nm='name',pr='price',qu='quantity',ty='type'))
        print('-'*85)
        for i in range(len(db)):
            if db[i].price>=g_price:
                print("|{nm:^20}|{pr:^20}|{qu:^20}|{ty:^20}".format(nm=db[i].name,pr=db[i].price,qu=db[i].quantity,ty=db[i].type))
                print('-'*85)

    def __str__(self):
        return self.name

1
dummy_obj=grocery('',0,0,'')
g1=grocery(nm='groundnut',pr='76',qu='1kg',ty='dal')
db.append(g1)
while True:
        dashboard()
        choice=input('enter your choice[1,2,3,4]:')

        if choice==1:
            dummy_obj.add_grocery_object()

        elif choice==2:
            if len(db)!=0:
                dummy_obj.display_grocery()
            else:
                print('no object in database...')
        elif choice==3:
            if len(db)!=0:
                dummy_obj.update_grocery()
            else:
                print('no object in database...')

        elif choice==4:
            if len(db)!=0:
                dummy_obj.delete_grocery()
            else:
                print('no object in database...')

        elif choice==5:
            if len(db)!=0:
                i=dummy_obj.search_grocery()
                if i>=0:
                    print('grocery price found in database')
                else:
                    print('grocery price not found in database')
            else:
                print('no object in database...')

        elif choice==6:
            if len(db)!=0:
                dummy_obj.price_grocery()
            else:
                print('invalid choice')

        ch=input('do you want to continue[y/n]:')
        if ch.lower()!='y':
            break




        

