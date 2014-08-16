# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def check(n, x, y):
    if x != y:
        print("failed check " + str(n))

check(1, False == 1 < 0, False)
check(2, False == (1 < 0), True)
check(3, False == 1, False)
check(4, False == 0, True)
check(5, False < 0, False)
check(6, False <= 0, True)
check(7, False + True + True, 2)
x = 3
x -= True
check(8, x, 2)
check(9, not 3, False)
check(10, not not 3, True)
# check(11, 1 + not not 3, 2)
check(12, 1 + (not not 3), 2)
check(13, 3 and 4, 4)
check(14, 4 and 3, 3)
check(15, 3 and not not 4, True)
