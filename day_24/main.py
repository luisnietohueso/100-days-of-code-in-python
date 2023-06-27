"""file = open('my_file.txt')
contents = file.read()
print(contents)
file.close()
"""
"""""
with open('my_file.txt') as file:
    contents = file.read()
    print(contents) 
"""
with open('C:/Users/Owner/Desktop/new.txt', mode='r') as file:
    file.read()
