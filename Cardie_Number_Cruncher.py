import numpy as np
import concurrent.futures
import time
#import multiprocessing as mp

start = time.perf_counter()

#an array of numbers 0-99
orig_array = np.arange(100)
#print("original array",'\n', orig_array)

#split array into an array of arrays of 10
array_chunks = ([orig_array[i*10:(i*10)+10] for i in range(0,10,1)])

#print("split arrays",'\n', array_chunks)

def summing_chunks(array_chunk):
    return sum(array_chunk)


def main():

    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:

        chunk_sums = []

        #this method does not work
        #for array, sum in zip(array_chunks, executor.map(summing_chunks, array_chunks)):
            #chunk_sums.append(sum)

        chunk_sums = list(executor.map(summing_chunks, array_chunks))

    #print("chunk_sums: ",'\n', chunk_sums)

    total_sum = sum(chunk_sums)
    print("total sum: ",'\n', total_sum)

if __name__ == '__main__':
    main()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds(s)')


#make an array for the sums of all the chunks
#array_of_sums = summing_chunks(array_chunks)


#print("==============================================================================================================================================")

#print("Array sums: ",'\n', array_of_sums)



























'''
#Create a ThreadPoolExecutor:
    #Up to 5 worker threads can run at the same time
    #executor is the object we’ll use to submit tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:


    #docs did warn: Calling Executor or Future methods from a callable submitted to a ProcessPoolExecutor will result in deadlock
    #that's why this line threw a BrokenProcessPool error when using ProcessPoolExecutor

    #For each array_chunk in the array_chunks list
        #Submit a task to executor to run summing_chunks(array_chunk)
            #This is asynchronous: they all start loading at the same time (roughly)
            #submit() immediately returns a Future object, which represents the ongoing task
    #Create a dictionary chunk_sums
        #future -> array_chunk (should be the sum of that chunk.....)
    chunk_sums = {executor.submit(summing_chunks, array_chunk) : array_chunk for array_chunk in array_chunks}

print("==============================================================================================================================================")

print("chunk_sums",'\n', chunk_sums)



#Go through the futures as they finish (not necessarily in the order we started them!)
    #as_completed() yields each future as soon as it’s done — perfect for seeing results immediately
for future in concurrent.futures.as_completed(chunk_sums):

    #Look up which array_chunk (should be the sum of that chunk!!!) this future was responsible for
    chunk_sum = chunk_sums[future]
    
    #append that sum to the array_of sums
    #seems to be appending that array_chunk....
    array_of_sums.append(chunk_sum)

print("==============================================================================================================================================")

print("sums of chunks",'\n', array_of_sums)
'''
