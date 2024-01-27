
def sumOfAllDivisors(n: int) -> int:
    import math
    sum_div = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            sum_div += i
        if i != n/i:
            sum_div+= n/i
    return sum_div


def sumOfAllDivisors(n: int) -> int:
    import math
    sum_div = 0
    for i in range(1,n):
        for j in range(1, int(n**0.5)+1):
            if i%j == 0:
                sum_div += j
            if j != i/j:
                sum_div+= i/j
    return sum_div

