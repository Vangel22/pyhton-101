movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
}
print(movie['title'])
# print(movie['budget'])
print(movie.get('budget'))
print(movie.get('budget', 'not found'))  # second param is message


movie.update({'title': 'The Holy Grail', 'year': 1975, 'cast': [
             'John', 'Eric', 'Michael', 'George', 'Terry']})
movie['budget'] = 250000
# del movie['year']
# print(movie)

year = movie.pop('year')
print(movie)
print(year)

for key, value in movie.items():
    print(key, value)


python = {'John': 35, 'Eric': 36, 'Michael': 35,
          'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35,
              'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35,
                 'Stan/Loretta': 32, 'Biccus Diccus': 45}
# membership test
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here!')

people = {}
people1 = {}
people2 = {}
# method 1 : update
people.update(python)  # updates the dictionary with the param key:values
people.update(holy_grail)
people.update(life_of_brian)

# print(people)
print(sorted(people.items()))


# method 2 : comprehension
for groups in (python, holy_grail, life_of_brian):
    # first is populated with python and then with holy_grail then with life_of_brian
    people1.update(groups)

# print(people1)
print(sorted(people1.items()))


# method 3 : unpacking - after version 3.5
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)  # this one has a different sort

print(sorted(people2.items()))
# print('The sum of the ages: ', sum(people.values))
# if one of the people.values is a string sum(people.values) is going to crash

# ** is used for dictionaries
# We can use * to unpack the list so that all elements of it can be passed as different parameters.
