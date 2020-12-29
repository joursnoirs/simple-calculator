print("Welcome to my Calculator")
print("Please type ? for help")

#a = base value
#num = input number

#history logs; log_to_hist is current function to obv log to history
hist = []
def log_to_hist(operation,num,a):
    hist.append(operation + str(num) + '=')
    hist.append(str(a))

num = 0.0
a = 0.0
operation = ""
while True:

    usei = input(str(a) + " ")
    #figuring out input
    if usei[0:1] in ['x', '*', '-', '/', '+']:
        operation = usei[0:1]
        if usei[1:].isnumeric():
            num = float(usei[1:]) 
    elif usei.isnumeric():
        num = float(usei)
        a = num
    elif usei[0:1] == '?':
        print("Type 'c' to clear current value.")
        print("Type 'q' to quit application.")
        print("Type 'h' to show a history of the program.")
    elif usei[0:1] == 'c':
        a = 0.0
        num = 0.0
    elif usei[0:1] == 'q': 
        print("Thanks for using my calculator :)")
        break
    elif usei[0:1] == 'h':
        for h in hist:
             print(h)
            
    else: print('Error! Did not understand Input. Use your brain!')
    #doing the math
    if operation != '' and num != None:
        if operation == '+': 
            a = a + num
        elif operation == '-': 
            a = a - num
        elif operation == 'x' or operation == '*': 
            a = a * num
        elif operation == '/': 
            a = a / num
        log_to_hist(operation, num, a)
    print("The answer is " + str(a) )
    operation = ""
