import numpy as np
import concurrent.futures
import time
import os

'''
summing an array of 100,000 numbers in parallel
math breakdown:
    10 processes
    array split - 10,000 arrays of 10 numbers
    chunksize = 100 -> 10 processes get 100 arrays at a time to process
'''

#an array of numbers 0-99999
orig_array = np.arange(100000)

#split array into an array of arrays of 10
#array_chunks holds 10,000 arrays of 10 numbers
array_chunks = ([orig_array[i*10:(i*10)+10] for i in range(0,10000,1)])

#summing_chunks takes an array_chunk of 10 numbers
#prints process ID of current process and the array_chunk that has been passed in
#returns the sum
def summing_chunks(array_chunk):
    print(f"Process {os.getpid()} is computing {array_chunk}...", '\n')
    return sum(array_chunk)

def main():
    
    #create the pool of "Process" objects (not to be confused w/ threads!)
    #that are named "executor"
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:

        start = time.perf_counter() #start timer

        #chunk_sums list holds a list of each of the sums of the 10,000 arrays
        #executor.map... 
            #makes each of the 10 processes run the summing_chunks(array_chunks[whatever])
        chunk_sums = list(executor.map(summing_chunks, array_chunks, chunksize=1000))
        finish = time.perf_counter() #stop timer

    #take the sum of the 10,000 sums to get the total sum
    total_sum = sum(chunk_sums)
    print("total sum: ",'\n', total_sum)

    #print time it took program to run in parallel
    print(f'Finished in {round(finish-start, 2)} seconds(s)')   

if __name__ == '__main__':
    main()




