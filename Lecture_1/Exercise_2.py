import os

def addition(a, b):
    os.system("cls" if os.name == "nt" else "clear")
    return a+b

def subtraction(a, b):
    os.system("cls" if os.name == "nt" else "clear")
    return a-b

def multiplication(a, b):
    os.system("cls" if os.name == "nt" else "clear")
    return a*b

def division(a, b):
    os.system("cls" if os.name == "nt" else "clear")
    return a/b

if __name__ == '__main__':
    while True:
        x = input('(1) for addition\n(2) for subtraction\n(3) for multiplication\n(4) for division\n(x) for exit\nInput >> ')
        if x == 'x':
            quit()
        elif int(x) in range(1, 5):
            x = int(x)
            while True:
                a = input("First number: ")
                b = input("Second number: ")
                if a.isdigit() and b.isdigit():
                    a = int(a)
                    b = int(b)
                    break
            # Code the different cases for arithmetics and the corresponding outputs. The functions for arithmetics are already coded. Hint: Use formatted strings and if-else-statements
            # Code start (8 Lines of Code)
            
            # Code end
        else:
            print("Not a valid input!")