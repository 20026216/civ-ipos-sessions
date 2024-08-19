# # Challenge 1 - Instructions
# A stack is a last-in, first-out (LIFO) data structure that allows elements to be 
# inserted and removed from the same end, called the top of the stack. 
# Your task is to create a Python class named Stack with the following methods:

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if
        return self.items.pop()


obj = Stack()
obj.push("aa")
obj.push("bb")
obj.pop()
print(obj.items)

# __init__: Initializes an empty stack.

# push(item): Adds an item to the top of the stack.
# pop(): Removes and returns the item at the top of the stack. 

# If the stack is empty, it returns None.
# is_empty(): Returns True if the stack is empty, False otherwise.