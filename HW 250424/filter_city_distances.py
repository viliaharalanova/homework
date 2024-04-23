city_distances = [
    ["Bansko", 97],
    ["Brussels", 1701],
    ["Alexandria", 1403],
    ["Nice", 1307],
    ["Szeged", 469],
    ["Dublin", 2479],
    ["Palermo", 987],
    ["Moscow", 1779],
    ["Oslo", 2098],
    ["London", 2019],
    ["Madrid", 2259]
]

for i in range(0,len(city_distances)):
    if city_distances[i][1] < 1500:
        print(f'{city_distances[i][0]} - {city_distances[i][1]}')