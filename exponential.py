import gmpy2

def is_square(n):
    if n < 0:
        return False
    
    sqrt_n = int(n**0.5)
    return sqrt_n * sqrt_n == n


for i in range(10000):
    #first = gmpy2.powmod(4, 2000, gmpy2.mpz(1))

    #second = gmpy2.pow(4, i, gmpy2.mpz(1))

    #third = gmpy2.pow(4, 2023, gmpy2.mpz(1))

    first = pow(gmpy2.mpz(4), 2000)

    second = pow(gmpy2.mpz(4), i)

    third = pow(gmpy2.mpz(4), 2023)

    result = first + second + third

    if is_square(result) == True:
        print(i)
        print('\n')


