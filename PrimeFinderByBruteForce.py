#1 Check if number 1 or above
#2 Check if number is 2 (the only even prime)
#3 Check if number is even
#4 If none of the above, check for odd divisors up to the square root of the number

import time
import math


def PrimeChecker(number):
    global calculationNum
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

    for i in range(3, squaredNum, 2):
        if number % i == 0:
            return False
    
    return True



def ClosestPrimeFinder(number):

    if PrimeChecker(number):
        return number
    
    i = 1

    while True:
        
        if PrimeChecker(number + i):
            return number + i
        
        elif number-1 > 0: 
            if PrimeChecker(number - i):
                return number - i
        
        i+=1

num = input("Input an integer to find closest prime:  ")

start_time = time.perf_counter()

# check if user input is all numbers
if num.isdigit():

    try:
        #try to convert num to int, if float raise error
            # Check if num is 0
        num = int(num)

        if num == 0:
            print("Integer must be a positive non zero number.")

        else:
            result = ClosestPrimeFinder(num)
            if result == num:
                print(f"{num:,} is a Prime Number!!!")
            else:
                print(f"{result:,} is the closest Prime Number to {num:,}. Difference: {result - num:,}")

    except ValueError:
        print("Please enter a valid positive integer.")
else:
    print("Please enter a valid positive integer.")

end_time = time.perf_counter()
print(f"Execution time: {end_time - start_time:.2f} seconds")