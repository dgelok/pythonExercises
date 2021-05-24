import math
from functools import lru_cache
def productFib(prod):
    # your code

    @lru_cache(maxsize=1000)
    def basic(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return basic(n - 1) + basic(n - 2)
    
    for i in range(math.floor(prod ** .5) + 1):
        if basic(i) * basic(i+1) == prod:
            return [basic(i), basic(i+1), True]
        if basic(i) * basic(i+1) > prod:
            return [basic(i), basic(i+1), False]


