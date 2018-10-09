# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

import mymodule
from mymodule import x
from mymodule import print_x

def set_x():
    global x
    x = 2

set_x()

print_x()
print(x)
