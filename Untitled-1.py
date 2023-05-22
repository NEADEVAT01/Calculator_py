while True: 
    arg = ''
    arg=input("Enter Math Function: ")
    if (arg == 'q'): break
    if (arg.isdigit() == False): print('Invalid function, try again ಠ_ಠ')
    else: print(arg,'=',eval(arg.replace('^','**')))   
    print('To exit type "q"')
exit() 
