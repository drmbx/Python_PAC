import sys
import math


def binom_coef(n: int, m: int) -> int:
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))


height = int(sys.argv[1])

for y in range(0, height):
    print(" " * (height - y - 1), end="")
    for x in range(0, y + 1):
        print(int(binom_coef(y, x)), end=" ")
    print()