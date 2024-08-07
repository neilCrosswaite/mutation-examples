def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def is_within_range(number, lower, upper):
    return lower <= number <= upper

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

