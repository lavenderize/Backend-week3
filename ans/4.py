# 4. 

animals = ('lion', 'tiger', 'penguin', 'dog', 'cat')

list_animals = list(animals)

for i in range(len(list_animals)):
    count = animals[i].count('e')
    if(count>0):
        del list_animals[i]

print(list_animals)


