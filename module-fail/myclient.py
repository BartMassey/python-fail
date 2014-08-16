import mymodule
from mymodule import *

def set_x():
    global x
    x = 2
    print_x()
    print(x)
    print()

set_x()

x = 2
print_x()
print(x)
print()

mymodule.x = 3
print_x()
print(x)
print(mymodule.x)
print()
