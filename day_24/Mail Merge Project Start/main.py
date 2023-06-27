# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
f = open('C:/Users/Owner/Desktop/python for everybody/day_24/Mail Merge Project Start/Input/Names/invited_names.txt',
         mode='r')
print(f.readlines())
names = ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']
# Replace the [name] placeholder with the actual name.
with open(
        'C:/Users/Owner/Desktop/python for everybody/day_24/Mail Merge Project Start/Input/Letters/starting_letter.txt',
        mode='r') as file:
    print(file.read())

# Save the letters in the folder "ReadyToSend".
txt = """Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela"""
for name in names[0:7]:
    x = txt.replace('[name]', name)
    filename = f'C:/Users/Owner/Desktop/python for everybody/day_24/Mail Merge Project Start/Output/letter_to_{name.strip()}'
    with open(filename, mode='w') as new_file:
        new_file.write(x)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
