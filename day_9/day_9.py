import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

people = []  # create empty list to store people's information

def add_person(name, bit):
  person = {'Name': name, 'Bit': bit}  # create dictionary with person's information
  people.append(person)  # add person's dictionary to list
  user()

def user():
  user_input = input('Do you want to add a person to the list? (yes/no): ')
  if user_input == 'yes':
    os.system('clear')  # clear the console
    print(logo)
    name = input('Enter the name of the person: ')
    bit = input('Enter the bit for the person: ')
    add_person(name, bit)  # call function to add person to list
  elif user_input == 'no':
    os.system('clear')
    print(logo)
    max_bit = people[0]['Bit']  # set max_bit to the bit of the first person in the list
    for person in people:
      if person['Bit'] > max_bit:
         max_bit = person['Bit']  # if a person's bit is greater than max_bit, update max_bit
    print(f'The highest bit in the list is {max_bit}')
  else:
    print('Invalid input:', user_input)

user()  # call user() function to start the program
