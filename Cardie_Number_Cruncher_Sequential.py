import numpy as np
import concurrent.futures
import time
import os

'''
summing an array of 100,000 numbers sequentially
math breakdown:
    1 process
    array split - 10,000 arrays of 10 numbers
    chunksize = 100 -> 1 process gets 100 arrays at a time to process
'''
#see the parallel version for more extensive version of comments

#an array of numbers 0-99
orig_array = np.arange(100000)

#split array into an array of arrays of 10
array_chunks = ([orig_array[i*10:(i*10)+10] for i in range(0,10000,1)])

def summing_chunks(array_chunk):
    print(f"Process {os.getpid()} is computing {array_chunk}...", '\n')
    return sum(array_chunk)

def main():

    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:

        start = time.perf_counter()
        chunk_sums = list(executor.map(summing_chunks, array_chunks, chunksize=1000))
        finish = time.perf_counter()

    total_sum = sum(chunk_sums)
    print("total sum: ",'\n', total_sum)

    print(f'Finished in {round(finish-start, 2)} seconds(s)')

if __name__ == '__main__':
    main()