# Written by Magnus Lie Hetland
import cython
cimport cython
import numpy as np
cimport numpy as np
import time
import random

"Everybody's favourite sorting algorithm... :)"

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = 0
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.

            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        split = partition(list, start, end)    # ... partition the sublist...
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return

#@cython.boundscheck(False)
cdef long cpartition(np.ndarray[np.float64_t, ndim=1] list, long start, long end):
    cdef np.float64_t pivot = list[end]                          # Partition around the last value
    cdef long bottom = start-1                           # Start outside the area to be partitioned
    cdef long top = end                                  # Ditto

    cdef long done = 0
    
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = 1                       # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.

            if top == bottom:                  # If we hit the bottom...
                done = 1                       # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    return top                                 # Return the split point


cpdef unsigned int cquicksort(np.ndarray[np.float64_t, ndim=1] list, long start, long end):
    cdef long split = 0
    if start < end:                            # If there are two or more elements...
        split = cpartition(list, start, end)    # ... partition the sublist...
        cquicksort(list, start, split-1)        # ... and sort both halves.
        cquicksort(list, split+1, end)
    else:
        return 0

n = int(1E6)
list = np.array([random.uniform(0, 1000) for ii in range(n)])
start = 0
end = n-1
list2 = np.copy(list)

time_begin = time.monotonic()
cquicksort(list, start, end)
print('cquicksort: ')
print(time.monotonic()-time_begin)

start = 0
end = n-1
time_begin2 = time.monotonic()
quicksort(list2, start, end)
print('quicksort: ')
print(time.monotonic()-time_begin2)
