numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0,len(numbers)):
    is_prime = 1
    is_prime1 = True
    is_prime2 = True
    if numbers[i] >= 2:
        for j in range(2,numbers[i]):
            if numbers[i] % j != 0:
                is_prime1 = True
            else: is_prime2 = False
            is_prime = is_prime1 * is_prime2
        if is_prime == 1:
            primes.append(numbers[i])
        else: not_primes.append(numbers[i])
print('primes : ',primes)
print('not_primes : ',not_primes)





