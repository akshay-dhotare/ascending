db = {101 : {'name': 'Jay', 'marks' : 88, 'roll' : 101, 'fees': 20000},
      102 : {'name': 'Pavan', 'marks' : 76, 'roll' : 102, 'fees': 25000},
      103 : {'name': 'Viru', 'marks' : 66, 'roll' : 103, 'fees': 15000},
    }

def dashboard():
    print('#'*60)
    print('\t\tWelcome to Student Management System by batch 459')
    print("""
                            menu
                            1) Create Student Record
                            2) Read All student
                            3) Update Stduent record
                            4) Delete Student Record
                            5) Display students by fees paid status
    """)

def create_student():
    u_name = input('Enter student name: ')
    u_roll = eval(input('Enter student roll: '))
    u_marks = eval(input('Enter student marks: '))
    u_fees = eval(input('Enter student fees paid: '))

    chotu_dict = {}

    chotu_dict['name'] = u_name
    chotu_dict['marks'] = u_marks
    chotu_dict['roll'] = u_roll
    chotu_dict['fees'] = u_fees

    db[u_roll] = chotu_dict
    print(f"Student {u_name} added successfully in db .....")
    print('*'*70)
    print()



def read_student():
    print('-'*60)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r='Roll number', n = 'Name', m='Marks',f='fees'))
    print('-'*60)
    for i in db:
        print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r=
        db[i]['roll'], n = db[i]['name'], m=db[i]['marks'],f=db[i]['fees']))
        print('-'*60)


def update_student():
    u_roll = eval(input('Enter student roll to update: '))
    if u_roll in db:
        u_name = input('Enter updated student name: ')
        # u_roll = eval(input('Enter student roll: '))
        u_marks = eval(input('Enter updated student marks: '))
        u_fees = eval(input('Enter updated student fees paid: '))

        db[u_roll]['name'] = u_name
        db[u_roll]['marks'] = u_marks
        db[u_roll]['fees'] = u_fees

        print(f"Student {db[u_roll]['name']} updated successfully in db .....")
        print('*'*70)
        print()





def delete_student():
    u_roll = eval(input('Enter student roll to delete: '))
    if u_roll in db:
        n = db[u_roll]['name']
        del db[u_roll]
        print(f"Student {n} deleted  successfully from db .....")
    else:
        print('Invalid Student Roll number...')

def read_student_fees():

    u_fees = eval(input('Enter student paid fees ammount to display: '))
    print('-'*60)
    print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r='Roll number', n = 'Name', m='Marks',f='fees'))
    print('-'*60)
    for i in db:
        if db[i]['fees'] >= u_fees:
            print("|{r:^15}|{n:^15}|{m:^15}|{f:^15}|".format(r=
            db[i]['roll'], n = db[i]['name'], m=db[i]['marks'],f=db[i]['fees']))
            print('-'*60)


while True:
    dashboard()
    choice = eval(input("Enter your choice [1,2,3,4]: "))
    print('-'*50)
    # print(choice)

    if choice == 1:
        create_student()

    elif choice == 2:
        if len(db) == 0:
            print('No student to display in data base ....')
        else:
            read_student()

    elif choice == 3:
        if len(db) == 0:
            print('No student to update in data base ....')
        else:
            update_student()

    elif choice == 4:
        if len(db) == 0:
            print('No student to delete in data base ....')
        else:
            delete_student()

    elif choice == 5:
        if len(db) == 0:
            print('No student to display in data base ....')
        else:
            read_student_fees()


    else:
        print('Invalid Choice....')

    ch = input('Do you want to Continue [y/n]: ')

    if ch.lower() != 'y':
        # print(db)
        break