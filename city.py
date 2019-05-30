import math
cities = [
{'city': 'Piter', 'price': 2000},
{'city': 'Moscow', 'price': 100},
{'city': 'Kiev', 'price': 700},
{'city': 'Mahachkala', 'price': 500},
]

middle = sum([c['price'] for c in cities])/len(cities)
lst = [math.fabs(middle-i['price']) for i in cities]
print(lst)
minimal = lst[0]
for i in range(len(lst)):
    if lst[i] < minimal:
        minimal = lst[i]
        city_inx = lst.index(minimal)
print(cities[city_inx])
