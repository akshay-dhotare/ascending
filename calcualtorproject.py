while True:
    print('*'*50)
    print('\t\t \U0001f600 Welcome to batch 459 Calculator \U0001f600')
    print('*'*50)

    print("""
                        Menu
                        + Addition
                        - Substraction
                        * Multiplication
                        / Division
                        **2 power of 2
                        % module

            """)
    choice = input("Enter your choice[+,-,*,/,**2,%] :")
    print(choice)
    print('-'*50)

    if choice == '+':
        new2_l = list(map(eval, input('').split(' ')))
        print(new2_l)
        s = 0
        for i in new2_l:
            s += i


        print('Addition is = ', s)

    elif choice == '-':
        new3_l = list(map(eval, input('').split(' ')))
        print(new3_l)
        s = 0
        for i in new3_l:
            s -= i
            
        print('substraction is =', s)    

    elif choice == '*':
        new4_l = list(map(eval, input('').split(' ')))
        print(new4_l)
        s = 0
        for i in new4_l:
            s *= i
            
        print('multiplication is =', s)  

    elif choice == '/':
        new5_l = list(map(eval, input('').split(' ')))
        print(new5_l)
        s = 0
        for i in new5_l:
            s /= i
            
        print('Division is =', s)
    elif choice == '%':
        new6_l = list(map(eval, input('').split(' ')))
        print(new6_l)
        s = 0
        for i in new6_l:
            s%2== i
    elif choice == '**2':
        new7_l = list(map(eval, input('').split(' ')))
        print(new7_l)
        s = 0
        for i in new7_l:
            s**2== i

    else:
        print('Invalid input/operation .....')



    ch = input('Do you want to continue [y/n] : ')
    if ch.lower() != 'y':
        break