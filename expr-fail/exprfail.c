#include <stdio.h>

void check(int n, int x, int y) {
    if (x != y)
        printf("failed check %d\n", n);
}

int main () {
    check(1, 0 == 1 < 0, 1); /* not 0 */
    check(2, 0 == (1 < 0), 1);
    check(3, 0 == 1, 0);
    check(4, 0 == 0, 1);
    check(5, 0 < 0, 0);
    check(6, 0 <= 0, 1);
    check(7, 0 + 1 + 1, 2);
    int x = 3;
    x -= 1;
    check(8, x, 2);
    check(9, !3, 0);
    check(10, !!3, 1);
    check(11, 1 + !!3, 2);
    check(12, 1 + (!!3), 2);
    check(13, 3 && 4, 1);  /* not 4 */
    check(14, 4 && 3, 1);  /* not 3 */
    check(15, 3 && !!4, 1);
    return 0;
}
