animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah', 'Zebra']

for animal in animals:  ## Q1
    try:  ##Q2
        if animal == 'Zebra':
            has_zebra = True
            break
        else:
            has_zebra = False

    except ValueError:
        print("I don't understand, please put a string")

print(has_zebra)

print("Has Zebra", "Zebra" in animals) ## THIS IS MORE EFFICIENT


#animals_names = []
#animals_traits = []
#for name in animals_dict:
#    animals_names.append(name)

#for key in animals_dict:
#    animals_traits.append(key)

#print(animals_names)
#print(animals_traits)

#animals_name = [name for name in animals_dict.keys()] ## better
#print(animals_name)

#for name in animal

animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
animals_dict['Giraffe'] = ''
animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Greg']
traits = ["Brave", "Fierce", "HUGE", "Tall", "Alright"]

animal_with_traits = zip(animals, traits)
print(animal_with_traits) ## THIS RETURNS A CLASS, the collection of letters and numbers is memory location
print(dict(animal_with_traits))


#for n,c in zip(animals, traits): ## returns a collection
#    animals[n] = c

animals = {n:c for n, c in zip(animals, traits)}