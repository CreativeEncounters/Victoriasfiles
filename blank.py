num1 = int(raw_input("num1:"))

operator = raw_input("operator:")

num2 = int(raw_input("num2:"))

if operator == '+':
    print num1+num2

if operator == '-':
    print num1-num2

if operator == '*':
    print num1*num2

if operator == '/':
    if num1 or num2 == 0:
        print "Cannot do operation"
    else:
        print num1/num2
    
   
    

