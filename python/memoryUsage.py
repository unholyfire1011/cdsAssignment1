#Code creates a matrix1 having 10000 elements doubles the numbers and stores it a new array and squares the numbers from first array and then stores it in seperate array.
import sys

def memory_test(): 
    # Step 1: Create first array
    array1 = list(range(10000))
    
    # Step 2: Create doubled array
    array2 = [x * 2 for x in array1]
    
    # Step 3: Create squared array  
    array3 = [x * x for x in array1]
    
    # Calculate memory usage
    mem1 = sys.getsizeof(array1) + sum(sys.getsizeof(x) for x in array1[:10])
    mem2 = sys.getsizeof(array2) + sum(sys.getsizeof(x) for x in array2[:10]) 
    mem3 = sys.getsizeof(array3) + sum(sys.getsizeof(x) for x in array3[:10])
    
    total_memory = (mem1 + mem2 + mem3) / (1024 * 1024)  # Convert to MB
    
    print(f"Array1 size: {len(array1)}")
    print(f"Array2 size: {len(array2)}")
    print(f"Array3 size: {len(array3)}")
    print(f"Total memory: {total_memory:.2f} MB")
    print(f"Sample values: {array1[100]}, {array2[100]}, {array3[100]}")
