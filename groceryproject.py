db={1:{'name':'gram','type':'dal','quantity':'1','price':'70'}}
def dashboard():
    print('#'*90)
    print("\t\t welcome to the grocery object list:")
    print('''          
                    menu
                    1)create grocery name
                    2)read all grocery
                    3)update grocery list
                    4)delete grocery list   ''')

def create_grocery():
    g_name=input('enter the grocery object:')
    g_type=input('enter the grocery type:')
    g_quantity=eval(input('enter the quantity of grocery:'))
    g_price=eval(input('enter the price of gocery:'))

    dict={}

    dict['name']=g_name
    dict['type']=g_type
    dict['quantity']=g_quantity
    dict['price']=g_price

    db[g_quantity]=dict
    print(f"grocery {g_name} added sucessfully in the db...")
    print('*'*90)
    print()

def read_grocery():
    print('-'*90)
    print("|{n:^15}|{t:^15}|{q:^15}|{p:^15}|".format(n='name',t='type',q='quantity',p='price'))
    print('-'*90)
    for i in db:
        print("|{n:^15}|{t:^15}|{q:^15}|{p:^15}|".format(n=db[i]['name'],t=db[i]['type'],q=db[i]['quantity'],p=db[i]['price']))
        print('-'*90)

def update_grocery():
    g_quantity=eval(input('enter grocery quantity to update:'))
    if g_quantity in db:
        g_name=input('enter grocery name to upadte:')
        g_type=input('enter grocery type to update:')
        g_price=eval(input('enter grocery price to update:'))

        db[g_quantity]['name']=g_name
        db[g_quantity]['type']=g_type
        db[g_quantity]['price']=g_price

        print(f"grocery {db[g_quantity]['name']} updated sucessfully in db ...")
        print('*'*90)
        print()

def delete_grocery():
    g_quantity=eval(input('enter the grocery quantity to delete:'))
    if g_quantity in db:
        n=db[g_quantity]['name']
        del db[g_quantity]
        print(f"grocery {n} deletd sucessfully from db...")
    else:
        print('invalid grocery')

while True:
    dashboard()
    choice=eval(input('enter your choice[1,2,3,4]:'))
    print('-'*90)

    if choice==1:
        create_grocery()
    elif choice==2:
        if len(db)==0:
            print('no grocery in data base...')
        else:
            read_grocery()

    elif choice==3:
        if len(db)==0:
            print('no grocery to update in data base..')
        else:
            update_grocery()

    elif choice==4:
        if len(db)==0:
            print('no grocery to delete in data base..')
        else:
            delete_grocery()
    else:
        print('invalid choice')

    ch=input('do you wantto continue[y/n]:')
    if ch.lower()!='y':
      break

