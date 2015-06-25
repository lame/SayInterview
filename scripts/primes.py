import random


def get_primes(n):

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
