import math 
import time

# slow method to bruteforce prime factors (takes about 2-5 min)
def print_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2),
        n = n / 2
    while n % 3 == 0:
        factors.add(3),
        n = n / 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            factors.add(i),
            n = n / i
        while n % (i + 2) == 0:
            factors.add(i + 2),
            n = n / (i + 2)
    if n > 3:
        factors.add(n)
    return sorted(factors)

# faster method (takes less than 1s)
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x-y), n)
    return d

def fast_factors(n):
    factors = []
    while n > 1:
        factor = pollards_rho(n)
        factors.append(factor)
        n //= factor
    return sorted(factors)

# to calculate private key d
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(e, phi_n):
    gcd, x, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi_n

def calculate_private_key(p, q, e):
    phi_n = (p-1)*(q-1)
    d = mod_inverse(e, phi_n)
    return d


start=time.time()

num = 24384827179940110397
e = 65537
# p, q = print_factors(num)
p, q = fast_factors(num)
print("The factors are:", p , "and", q)
print("The private key is:", calculate_private_key(p, q, e))

end=time.time()
diff=end-start
print("Time taken:",diff,"s")


