#Performing increasingly large matrix multiplications (50x50 to 100x100)
import time
import random
import sys
import tracemalloc

def generate_matrix(size):
    return [[random.random() for _ in range(size)] for _ in range(size)]

def matrix_multiply(a, b):
    size = len(a)
    result = [[0.0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += a[i][k] * b[k][j]
    return result

def test_stability(load_factor):
    tracemalloc.start()
    
    start_time = time.time()
    matrix_size = int(50 * load_factor)
    
    # Generate matrices
    a = generate_matrix(matrix_size)
    b = generate_matrix(matrix_size)
    
    # Perform multiplication
    result = matrix_multiply(a, b)
    
    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return {
        "load_factor": load_factor,
        "matrix_size": matrix_size,
        "time_sec": elapsed_time,
        "memory_current_mb": current / (1024 * 1024),
        "memory_peak_mb": peak / (1024 * 1024)
    }

if __name__ == "__main__":
    print("Python Stability Under Load Test")
    print("Load Factor | Matrix Size | Time (sec) | Current Mem (MB) | Peak Mem (MB)")
    print("-" * 80)
    
    for load in [0.5, 1.0, 1.5, 2.0]:
        results = test_stability(load)
        print(f"{results['load_factor']:10.1f} | {results['matrix_size']:11d} | {results['time_sec']:10.3f} | {results['memory_current_mb']:15.2f} | {results['memory_peak_mb']:12.2f}")
Java:-
