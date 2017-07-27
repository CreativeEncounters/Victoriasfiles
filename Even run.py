def iseven(num):
    if num % 2 == 0:
        return 'even!'
    else:
        return 'odd!'

for i in range(0,20):
    result = iseven(i)
    print i, result
