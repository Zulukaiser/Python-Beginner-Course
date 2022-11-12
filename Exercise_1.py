from string import ascii_lowercase

# import the factorial function from the math module
# Code start (1 Line of code)

# Code end

# import the variable ARR and NUMBERS from the file data.py
# Code start (1 Line of code)

# Code end


# define a function called 'isValid' where you give a variable and try to evaluate if the given variable only contains characters. If not, raise a ValueError with the decription 'Variable contains a non character type!'
# remember to loop through the string that is given as the argument. Use formatted strings for the error message
# Code start (4 Lines of code)

# Code end

def getInput():
    x = input('Input an integer: ')
    # Code a try and except instruction that tests if x is an integer. The exception should print 'Not an Integer!'
    # Code start (4 Lines of code)

    # Code end

# Code the main function, so that the code can run as a script
# Code start (1 Line of code)

# Code end
    getInput()
    # loop through the 'NUMBERS' variable and print the factorial of the number as 'The factorial of x is: factorial(x)'. Use formatted strings for the print function
    # Code start (3 Lines of code)

    # Code end
    for i in ARR:
        isValid(i)
        print(i)