#Filter people under 18 and map remaining names
people = [
    {"name": "Goku", "age": 55},
    {"name": "Vegeta", "age": 46},
    {"name": "Gohan", "age": 10},
    {"name": "Frieza", "age": 27}
]
adults = list(filter(lambda person: person["age"] >= 18, people))
names = list(map(lambda person: person["name"], adults))
print(names)
