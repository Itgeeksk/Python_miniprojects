
# Making a function name fabonacci
def fabonacci(num):
    # checking the num is postive or negative
    if num < 0 :
        print('Incorrect value for fabonacci')
    # Checking value is 0 or not
    elif num == 0:
        return 0
    # checking the value is 1 or 2
    elif num == 1 or num == 2:
        return 1
    else:
        # returning fabonacci of the num   [Fn = Fn-1 + Fn-2]
        return fabonacci(num-1) + fabonacci(num-2)
    
# Calling fabonacci function
result = fabonacci(9)
# Printing the function on screen
print(result)

 