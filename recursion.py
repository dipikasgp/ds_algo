def print1toN(i, n):
    if i > n:
        return
    print(i)
    print1toN(i + 1, n)


def print1toN_backtrack(i, n):
    if i < 1:
        return
    print1toN_backtrack(i - 1, n)
    print(i)


def printNto1(i, n):
    if i < 1:
        return
    print(i)
    print1toN(i - 1, n)


# parameterised
def sum_n_numbers(i, sum):
    if i < 1:
        return sum
    sum_n_numbers(i - 1, sum)


# functional
def sum_n_numbers_func(n):
    if n == 0:
        return 0
    return n + sum_n_numbers_func(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def reverse_array(arr, i, n):
    if i > n / 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse_array(arr, i + 1, n)


def check_str_palindrome(s, i, n):
    if i > n / 2: return True
    if s[i] != s[n - i - 1]:
        return False
    check_str_palindrome(s, i + 1, n)


def nth_fibonacii(n):
    if n <= 1:
        return n
    return nth_fibonacii(n - 1) + nth_fibonacii(n - 2)
