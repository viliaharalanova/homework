user_list = []
name_count = int(input('How many names are you going to enter? '))

for i in range(0, name_count):
    name = input('Enter a name, please: ')
    user_list.append(name)
    i+=1

print(user_list)