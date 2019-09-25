"""[this algorithm computes the largest contigous values in an array]
    in O(n)
    the contigous values are also known as subarray
"""
# Steps are sourced from geeksforgeeks
#Link https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""
    Lets take the example:
    [-2, -3, 4, -1, -2, 1, 5, -3]

    max_so_far = max_ending_here = 0

    for i=0,  a[0] =  -2
    max_ending_here = max_ending_here + (-2)
    Set max_ending_here = 0 because max_ending_here < 0

    for i=1,  a[1] =  -3
    max_ending_here = max_ending_here + (-3)
    Set max_ending_here = 0 because max_ending_here < 0

    for i=2,  a[2] =  4
    max_ending_here = max_ending_here + (4)
    max_ending_here = 4
    max_so_far is updated to 4 because max_ending_here greater 
    than max_so_far which was 0 till now

    for i=3,  a[3] =  -1
    max_ending_here = max_ending_here + (-1)
    max_ending_here = 3

    for i=4,  a[4] =  -2
    max_ending_here = max_ending_here + (-2)
    max_ending_here = 1

    for i=5,  a[5] =  1
    max_ending_here = max_ending_here + (1)
    max_ending_here = 2

    for i=6,  a[6] =  5
    max_ending_here = max_ending_here + (5)
    max_ending_here = 7
    max_so_far is updated to 7 because max_ending_here is 
    greater than max_so_far

    for i=7,  a[7] =  -3
    max_ending_here = max_ending_here + (-3)
    max_ending_here = 4 """
# the idea here is to reset max_ending_here if the current max_ending_here is less than 
# 0 and i is less than 0
a = [-13, -3, -25, 20, -3, 16, -23, -12, -5, -22, -15, 4, -7] 
def max_sub_array(array):
    """
    This only works for an array with atleast a single positive member, it wii 
    return 0 if false.
    
    Arguments:
        array {[list]} 
    
    Returns:
        [int] 
    """
    array_size = len(array)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, array_size):
        #increment max_ending_here first by the current value at index i
        max_ending_here = max_ending_here + array[i]
        # then check if the max_ending_here is less than 0; if it is then that means up to the current
        # index i there is no way it will form part of the subarray(this is very important and forms the idea
        # behind this algorithm) 
        if  max_ending_here < 0:
            max_ending_here = 0
        # lets check if max_ending_here > max_so_far only if max_ending here is > 0
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far
print(max_sub_array(a))
# prints 33
