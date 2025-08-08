#Attempt to open a file "numbers.txt" (Will contain some erroneous inputs)
#Read numbers line by line
#Calculate square roots (handling negative numbers)
#Sum all valid square roots
#Handle file I/O errors, number format errors, and mathematical errors
#Output the final sum or appropriate error messages

import time
import math
import tracemalloc
import sys

def calculate_square_roots():
    tracemalloc.start()
    start_time = time.perf_counter()
    
    try:
        with open("numbers.txt", "r") as file:
            lines = file.readlines()
            total_sum = 0.0
            
            for line_number, line in enumerate(lines, 1):
                try:
                    number = float(line.strip())
                    if number < 0:
                        print(f"Warning: Negative number on line {line_number}, skipping", file=sys.stderr)
                        continue
                    sqrt = math.sqrt(number)
                    total_sum += sqrt
                except ValueError:
                    print(f"Error: Invalid number format on line {line_number}", file=sys.stderr)
            
            print(f"Total sum of square roots: {total_sum}")
    
    except FileNotFoundError:
        print("Error: File not found - numbers.txt", file=sys.stderr)
    except PermissionError:
        print("Error: No permission to read the file", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
    
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print("\nProfiling Results:")
    print(f"Time taken: {(end_time - start_time) * 1e6:.2f} µs")
    print(f"Memory used: {peak / 1024:.2f} KB")

if __name__ == "__main__":
    calculate_square_roots()
