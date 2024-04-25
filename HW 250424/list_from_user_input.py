user_list = []
name_count = int(input('How many names are you going to enter? '))

for i in range(name_count):
    name = input('Enter a name, please: ')
    user_list.append(name)
    i+=1

for name in user_list:
    print(name)