a = {'Mary': 'm@a.com', 'John': 'j@x.com'}
print(a['Mary'])

print(a['john'])
a[23] = 'Y'
print(a)

del a['Mary']
print(a)

for x in a:
    print(x)

for x in a.keys():
    print(x)

for k, v in a.items():
    print(k, v)

categories = ["Frozen", "Produce", "Canned", 
              "Frozen", "Canned", "Canned", 
              "Produce", "Produce"]
foods = ["Pizza", "Oranges", "Chickpeas", 
         "Popsicles", "Beans", "Olives", 
         "Pears", "Grapes", "Butter"]

dict_cat = {}
for cat, food in zip(categories, foods):
    if cat in dict_cat:
        dict_cat[cat].append(food)
    else:
        dict_cat[cat] = [food]