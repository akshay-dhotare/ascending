db={101:{'name':'saurabh','id':101,'salary':20000,'post':'manager'}}
def dashboard():
    print("\t\t welcome to employee management system")
    print("""         menu
                1.create employee profile
                2.read employee profile
                3.update employee profile
                4.delete employee profile
                                                  """)

def create_employee():
    e_name=input("enter your name :-")
    e_id=eval(input("enter employee id :-"))
    e_salary=eval(input("enter employee salary :-"))
    e_post=input("enter employee post :-")
    dict={}

    dict['name']=e_name
    dict['id']=e_id
    dict['salary']=e_salary
    dict['post']=e_post

    db[e_id]=dict
    print(f"employee {e_name} added successfully in data base...")
    print('*'*64)

def read_employee():
    print('_'*64)
    print("|{id:^15}|{n:^15}|{s:^15}|{p:^15}|".format(id='id number',n='name',s='salary',p='post'))
    for i in db:
     print("|{id:^15}|{n:^15}|{s:^15}|{p:^15}|".format(id=db[i]['id'],n=db[i]['name'],s=db[i]['salary'],p=db[i]['post']))
     print('*'*64)

def update_employee():
    e_id=eval(input("enter your employee id no.:-"))
    if e_id in db:
       e_name=input("enter your name :-")
       e_salary=eval(input("enter employee salary :-"))
       e_post=input("enter employee post :-")

       db[e_id]['name']=e_name
       db[e_id]['salary']=e_salary
       db[e_id]['post']=e_post

       print(f"employee profile {db[e_id]['name']}successfully updated in data base...")
       print('*'*64)
def delete_employee():
    e_id=eval(input("enter employee id no for delete.."))
    if e_id in db:
        n=db[e_id]['name']
        del db[e_id]
        print(f"employee {n} deleted successfully from data base..")
    else:
        print("invalid employee id number..")


while True:
  dashboard()
  choice=eval(input("enter your choice [1,2,3,4]:"))
  print(choice)
  if choice==1:
    create_employee()

  elif choice==2:
    if len(db)==0:
        print("data not found..")
    else:
        read_employee()


  elif choice==3:
    if len(db)==0:
        print("no empolyee update in data base...")
    else:
       update_employee()

  elif choice==4:
    if len(db)==0:
        print("no employee data avaliable for deleting....")
    else:
        delete_employee()

  else:
    print("invalid choice..")
 
  ch=input("do you want to continue [y/n]:")
  if ch.lower()!='y':
    break