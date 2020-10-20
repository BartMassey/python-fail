# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

x = 3

def f():
    # The `x` here refers to the local variable *defined on
    # the next line*!  It thus is "referenced before
    # assignment".
    print(x)
    # This creates a new local `x` that shadows the global
    # `x`. It does not alter the global `x`.
    x = 4
    print(x)

f()
