import time

upper = int(input("Enter the range upto which the prime numbers have to be printed "))

primes = [2,3,5,7]

for num in range(3,upper):
    if all(num%x != 0 for x in primes):
       primes.append(num)
time.sleep(5.0)
print( primes)
