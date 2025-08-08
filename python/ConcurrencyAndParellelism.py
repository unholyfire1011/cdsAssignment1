#Spawn multiple threads and perform a CPU-bound task (summing numbers) and then measure execution time.
from multiprocessing import Process, Value
import time

def sum_numbers(start, end, result):
    with result.get_lock():
        result.value += sum(range(start, end))

def main():
    start_time = time.time()
    result = Value('i', 0)
    processes = []

    for i in range(4):
        p = Process(
            target=sum_numbers,
            args=(i * 250_000, (i + 1) * 250_000, result)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Multiprocessing result: {result.value}, Time: {time.time() - start_time:.3f}s")

if __name__ == "__main__":
    main()
