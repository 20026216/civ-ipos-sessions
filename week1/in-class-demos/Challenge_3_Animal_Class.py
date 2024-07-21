animals_dict = {'Lion': 'Brave', 'Tiger': 'Fierce', 'Elephant': 'Large', 'Giraffe': 'Tall', 'Zebra': 'Striped'}
class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic

    # def get_animal_with_characteristic(self, name, characteristic): I tried rip
    #     animals_with_characteristics = []
    #     for name, characteristic in animals_dict.items():
    #         animal = Animal(name, characteristic)
    #         animals_with_characteristics.append(animal)
    #     return animals_with_characteristics

    # def __repr__(self): This allows string representation of an instance, rather than object and its memory location
    #     return f"Animal(name='{self.name}', characteristic='{self.characteristic}')"


# lion = Animal('Lion', 'King')
# lion.modify_characteristic('Brave')


# Create instances of Animal for each entry in animals_dict
animals = []
for name, characteristic in animals_dict.items():
    animal = Animal(name, characteristic)
    animals.append(animal)

print(animals[0])
# Print the list of animal instances
for animal in animals:
    print(animal.name + " " + animal.characteristic)
