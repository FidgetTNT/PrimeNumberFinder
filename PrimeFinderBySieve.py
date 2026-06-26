#1 Check if number 1 or above
#2 Check if number is 2 (the only even prime)
#3 Check if number is even
#4 If none of the above, check for odd divisors up to the square root of the number

import time
import math
import csv

memo = []


def prime_checker(number):
    global memo
    # Check if number is 1 or below
    if number < 2:
        return False

    # Check if number is 2
    if number == 2:
        return True
    
    # Check if number is even
    if number % 2 == 0:
        return False

    # Check all odd divisors up to the square root of the number
    squaredNum = math.ceil(math.sqrt(number))
    
    if len(memo) == 0 or max(memo)**2 < number:
        sieve_with_next(squaredNum)
        with open("List_Of_Primes.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            memo = [int(x[0]) for x in reader]


    for i in range(len(memo)):
        if number % memo[i] == 0:
            return False
            
    return True

#using Sieve of Eratosthenes method
def sieve(limit):

    is_prime = [True] * ((limit//2) + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for multiple in range(i * i, (limit//2) + 1, i):

                is_prime[multiple] = False

    return [i for i, prime in enumerate(is_prime) if prime]

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def sieve_with_next(limit):
    primes = sieve(limit)

    candidate = limit + 1

    while not is_prime(candidate):
        candidate += 1

    primes.append(candidate)

    with open("List_Of_Primes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in primes:
            writer.writerow((row,))


def ClosestPrimeFinder(number):
    global memo
    with open("List_Of_Primes.csv", mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        memo = [int(x[0]) for x in reader]

    if prime_checker(number):
        return number
    
    i = 1

    while True:
        
        if prime_checker(number + i):
            return number + i
        
        elif number-1 > 0:
            if prime_checker(number - i):
                return number - i
        
        i+=1

num = input("Input an integer to find closest prime:  ")

start_time = time.perf_counter()

# check if user input is all numbers
if num.isdigit():

    #try:
        #try to convert num to int, if float raise error
            # Check if num is 0
        num = int(num)

        if num == 0:
            print("Integer must be a positive non zero number.")

        else:
            print(f"Square root: {math.ceil(math.sqrt(num))}")
            result = ClosestPrimeFinder(num)
            if result == num:
                print(f"{num:,} is a Prime Number!!!")
                print(f"Highest prime in memory: {max(memo)}")
                
            else:
                print(f"{result:,} is the closest Prime Number to {num:,}. Difference: {result - num:,}")
                print(f"Highest prime in memory: {max(memo)}")
                

    #except ValueError:
        #print("Please enter a valid positive integer.")
else:
    print("Please enter a valid positive integer.")


end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.2f} seconds")