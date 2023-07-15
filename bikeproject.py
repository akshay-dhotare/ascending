db={1:{'name':'cd100','year':'1998','amount':'50000','product':'two wheeler'}}
def dashboard():
    print('#'*90)
    print("\t\t welcome to bike showroom product")
    print('''     menu
                 1) create bike record
                 2) read  bike record
                 3)update bike  record
                 4)delete bike   record      ''')

def create_bike():
    b_name=input('enter the name of bike:')
    b_year=eval(input('enter the manufactuing year:'))
    b_amount=eval(input('enter the price:'))
    b_product=input('enter the product type:')
    
    dict={}

    dict['name']=b_name
    dict['year']=b_year
    dict['amount']=b_amount
    dict['product']=b_product

    db[b_amount]=dict
    print(f"bike {b_name} added sucessfully in the data base..")
    print('*'*90)
    print()

def read_bike():
    print('-'*90)
    print("|{y:^15}|{n:^15}|{a:^15}|{p:^15}|".format(y='year',n='name',a='amount',p='product'))
    print('-'*90)
    for i in db:
        print("|{y:^15}|{n:^15}|{a:^15}|{p:^15}|".format(y=db[i]['year'],n=db[i]['name'],a=db[i]['amount'],p=db[i]['product']))
        print('*'*90)

def update_bike():
    b_amount=eval(input('enter the amount to update:'))
    if b_amount in db:
        b_name=input('enter the  updated  bike name:')
        b_year=eval(input('enter the updated manufacturing year:'))
        b_product=input('enter the updated product type:')

        db[b_amount]['name']=b_name
        db[b_amount]['year']=b_year
        db[b_amount]['product']=b_product

        print(f"bike name{db[b_amount]['name']}sucessfully updated in data base...")
        print('*'*90)
        print()

def delete_bike():
    b_amount=eval(input('enter the amount for delete:'))
    if b_amount in db:
        n=db[b_amount]['name']
        del db[b_amount]
        print(f"bike {n} sucessflly deleted from data base...")
    else:
        print("invalid bike product...")


while True:
    dashboard()
    choice=eval(input('enter your choice[1,2,3,4]:'))
    print('-'*90)
    print(choice)
    if choice==1:
        create_bike()

    elif choice==2:
        if len(db)==0:
            print('data not found..')
        else:
            read_bike()

    elif choice==3:
        if len(db)==0:
            print('no bike update in data base..')
        else:
            update_bike() 

    elif choice==4:
        if len(db)==0:
            print('no bike available for deleting..')
        else:
            delete_bike()

    else:
        print('inavalid choice..')

    ch=input('do you want to continue[y/n]:')
    if ch.lower()!='y':
      break 