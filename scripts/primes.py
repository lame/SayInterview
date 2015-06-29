import random
from math import sqrt


def fermat(n=100):

    prime_list = []

    if n >= 1 and n <= 3:
        for x in range(1, n+1):
            prime_list.append(x)
    elif n > 2:
        a = random.randint(2, n-1)
        prime_list = [1, 2]

        for x in range(3, n, 2):
            if (a ** x % x == a % x):
                prime_list.append(x)

    return prime_list

def get_primes(n=100):
    prime_list = []

    if n >= 1 and n <= 3:
        for x in range(1, n+1):
            prime_list.append(x)
    elif n > 2:
        prime_list = [1, 2]

        for x in range(3, n, 2):
            if is_prime(x):
                prime_list.append(x)

    return prime_list

def is_prime(n):
    for z in range(2, int(sqrt(n)+1)):
        if not n % z:
            return False
    return True
