# Copyright © 2014 Bart Massey
# For some reason, nil [] is an lvalue. 
# This can be really confusing.

x = []
y = []
x += [1]
y += [2]
print(x, y)

x = []
y = x
x += [1]
y += [2]
print(x, y)
