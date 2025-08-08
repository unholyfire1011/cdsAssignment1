#Generate all prime numbers up to a fixed limit (LIMIT = 500,000) using the Sieve of Eratosthenes algorithim.
#Simulate additional memory load by storing extra data for each prime.
#Measure and print the memory usage.

import psutil
import os

LIMIT = 500000

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)  # MB

def main():
 
    
    start_memory = get_memory_usage()
    
    # Create large boolean list
    sieve = [True] * (LIMIT + 1)
    sieve[0] = sieve[1] = False
    
    # Sieve algorithm
    p = 2
    while p * p <= LIMIT:
        if sieve[p]:
            for i in range(p * p, LIMIT + 1, p):
                sieve[i] = False
        p += 1
    
    # Collect primes and create memory pressure
    primes = []
    extra_data = []
    
    for i in range(2, LIMIT + 1):
        if sieve[i]:
            primes.append(i)
            # Add memory pressure
            temp = [i + j for j in range(50)]
            extra_data.append(temp)
    
    peak_memory = get_memory_usage()
    
    print(f"Start memory: {start_memory:.1f} MB")
    print(f"Peak memory: {peak_memory:.1f} MB")
    print(f"Memory used: {peak_memory - start_memory:.1f} MB")

if __name__ == "__main__":
    main()
