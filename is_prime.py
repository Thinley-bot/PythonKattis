# define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# define a function to find all prime numbers in a given range
def find_primes_in_range(start, end):
    primes = []
    for i in range(start, end+1):
        if is_prime(i):
            primes.append(i)
    return primes

# test the function
start = 10
end = 50
primes = find_primes_in_range(start, end)
print("Prime numbers between", start, "and", end, "are:", primes)
