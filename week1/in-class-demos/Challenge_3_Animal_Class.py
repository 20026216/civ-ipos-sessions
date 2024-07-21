class Animal:
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def modify_characteristic(self, new_characteristic):
        self.characteristic = new_characteristic

lion = Animal('Lion', 'King')
lion.modify_characteristic('Brave')

print(lion.characteristic)
print(lion.name)
