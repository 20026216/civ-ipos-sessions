'''different ways to reuse the same code
as a module'''

import greeter
greeter.greet()

# use an alias - consider why might we do this?


import greeter as g
g.greet()

# sometimes we only want to import what we need


from greeter import greet
greet()

# Additional Activity create a calculator class in the module

from greeter import Calculator

# Use the new class to return a score to a user
#
# Addition1 = Calculator(1, 2)
#
# result = Addition1.add()
calculator = greeter.Calculator()

result = calculator.add(2,3)

print(f"Result of addition: {result}")