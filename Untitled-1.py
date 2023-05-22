while True: 
    arg = ''
    arg=input("Enter Math Function: ")
    if (arg == 'q'): break
    try:
        print(arg,'=',eval(arg.replace('^','**'))) 
    except NameError:
        print('Invalid function, try again ಠ_ಠ')
    print('To exit type "q"')
exit() 