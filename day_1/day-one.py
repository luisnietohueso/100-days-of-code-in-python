# printing few inputs
def prin():
    print(len(input("What is your name? ")))
    print("Day 1 - String Manipulation")
    print('String Concatenation is done with the "+" sign.')
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")


prin()


# Write a program that switches the values stored in the variables a and b
def switches():
    a = input("a: ")
    b = input("b: ")
    c = a
    a = b
    b = c
    print("a: " + a)
    print("b: " + b)


switches()


# this function will create a few question and give you and idea for a band name
def band():
    print("Welcome to the Band Name Generator.")
    x = input('which is the name of your city?\n')
    y = input('which is the name of your pet?\n')
    print('the name of your band can be :' + x + ' ' + y)


band()
