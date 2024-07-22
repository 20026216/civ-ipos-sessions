animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}


class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic

    # def __repr__(self): This allows string representation of an instance, rather than object and its memory location
    #     return f"Animal(name='{self.name}', characteristic='{self.characteristic}')"


# Create instances of Animal for each entry in animals_dict


animals = []
for animal_name, animal_characteristic in animals_dict.items():
    animal = Animal(animal_name, animal_characteristic)
    animals.append(animal)

# only gives you info about the Animal object existing in the specified memory address
print(animals[0], "\n")

# This breaks it down to its key and value names
print(animals[1].name + " " + animals[1].characteristic, "\n")

# Print the list of animal instances
for animal in animals:
    print(animal.name + " " + animal.characteristic)
