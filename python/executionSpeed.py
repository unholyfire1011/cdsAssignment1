# Code that Calculate sum of numbers 1 to 1,000,000, repeat 10 times
import cProfile #profiling tool used

def calculate_sum():
    total = 0
    for i in range(10):
        total += sum(range(1, 1000001))
    return total

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    
    result = calculate_sum()
    
    profiler.disable()
    profiler.print_stats()
    print(f"Result: {result}")
