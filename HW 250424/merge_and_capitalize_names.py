first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]
full_names = []

for i in range(len(first_names)):
    fn = first_names[i].capitalize()
    sn = sur_names[i].capitalize()
    full_names.append(f'{fn} {sn}')

print(full_names)
