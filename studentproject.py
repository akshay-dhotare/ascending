db={101:{'name':'jay','roll':'101','marks':'88','fees':'25000'},
    102:{'name':'pavan','roll':'102','marks':'76','fees':'20000'},
    103:{'name':'viru','roll':'103','marks':'66','fees':'15000'}}


def dashboard ():
    print('welcome to student mangement system')
    print(""" 
                  menu
                  1) create student record
                  2)read student record
                  3)update student record
                  4)delete record
                  5)display student by fees paid status
                  6)display student by marks """  )

def create_student():
    u_name=input('enter your name:')
    u_roll=eval(input('enter your roll:'))
    u_marks=eval(input('enter your marks:'))
    u_fees=eval(input('enter your fees:'))

    chotu_dict={}

    chotu_dict['name']=u_name
    chotu_dict['marks']=u_marks
    chotu_dict['roll']=u_roll
    chotu_dict['fees']=u_fees

    db[u_roll]=chotu_dict
    print(f"student{u_name} added sucessfully in db ....")
    print('*'*90)
    print()


def read_student():
    print('_'*90)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r='roll number',n='name',m='marks',f='fees'))
    print('-'*90)
    for i in db:
        print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r=db[i]['roll'],n=db[i]['name'],m=db[i]['marks'],f=db[i]['fees']))
        print('-'*90)



    
    


