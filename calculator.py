while True: 
    arg=input("Enter Math Function: ")
    if (arg == 'q'): break
    if (arg.isdigit() == True): print(arg,'=',eval(arg.replace('^','**'))) 
    else: print('Invalid function, try again ಠ_ಠ')
    print('To exit type "q"')
exit() 
