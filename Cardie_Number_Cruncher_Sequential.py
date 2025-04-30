import numpy as np
import concurrent.futures
import time

#an array of numbers 0-99
orig_array = np.arange(100000)
print("original array",'\n', orig_array)

#split array into an array of arrays of 10
array_chunks = ([orig_array[i*10:(i*10)+10] for i in range(0,10000,1)])

print("split arrays",'\n', array_chunks)

def summing_chunks(array_chunk):
    return sum(array_chunk)


def main():

    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:

        chunk_sums = []

        start = time.perf_counter()
        chunk_sums = list(executor.map(summing_chunks, array_chunks, chunksize=1000))
        finish = time.perf_counter()
    
    print("chunk_sums: ",'\n', chunk_sums)

    total_sum = sum(chunk_sums)
    print("total sum: ",'\n', total_sum)

    print(f'Finished in {round(finish-start, 2)} seconds(s)')

if __name__ == '__main__':
    main()