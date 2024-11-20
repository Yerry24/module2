numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in numbers:
        if j == 1:
            continue
        if i // j > 1 and i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True:
        primes.append(i)
print('Primes: ',primes)
print('Not_primes: ',not_primes)