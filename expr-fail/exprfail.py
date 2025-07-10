# Copyright © 2014 Bart Massey
# [This program is licensed under the "MIT License"]
# Please see the file COPYING in the source
# distribution of this software for license terms.

def check(n, x, y):
    if x is not y:
        print("failed check " + str(n))

# Precedence of == and < are the same, so they go
# left-to-right. The 1 is autoconverted to True.
check(1, False == 1 < 0, False)
# Presumably what was intended by above.
check(2, False == (1 < 0), True)
# This seems reasonable.
check(3, False == 1, False)
# These less so. Probably these autoconversions in
# comparisons should not happen, but they do.
check(4, False == 0, True)
check(5, False < 0, False)
check(6, False <= 0, True)
# These are reasonable, maybe.
check(7, False + True + True, 2)
x = 3
x -= True
check(8, x, 2)
# 3 is autoconverted to True.
check(9, not 3, False)
# Here also.
check(10, not not 3, True)
# This is a syntax error rather than an autoconversion for
# some reason.
#check(11, 1 + not not 3, 2)
# Now 3 will be autoconverted, and the True will be
# autoconverted back.
check(12, 1 + (not not 3), 2)
# "and" and "or" don't autoconvert their arguments, but
# just preserve them.
check(13, 3 and 4, 4)
check(14, 4 or 3, 4)
# But "not" has to autoconvert.
check(15, 3 and not not 4, True)
