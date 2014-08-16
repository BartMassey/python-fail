# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

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
