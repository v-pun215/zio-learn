#mergesort
'''
Merge sort functionality:
(1) - Split array into 2 parts from middle index
(2) - Sort each half seperately (recursively)
(3) - Merge the arrays using:
    ---> 1. compare first element of both arrays to merge, add smaller number to new array
    ---> 2. repeat recursively until no elements left/ only one element left (added last)
    ---> 3. recursively rinse and repeat untill all arrays have been merged
'''
def merge_arrays(left_halve, right_halve):
    i, j = 0, 0
    merged_array = []

    while i < len(left_halve) and j < len(right_halve):
        if left_halve[i] <= right_halve[j]:
            merged_array.append(left_halve[i])
            i+=1
        else:
            merged_array.append(right_halve[j])
            j+=1

    if i < len(left_halve):
        merged_array.extend(left_halve[i:])
    if j < len(right_halve):
        merged_array.extend(right_halve[j:])

    return merged_array



def mergesort(arr):
    if len(arr) <=1:
        return arr
    total_len = len(arr) # get total number of items in list
    left_halve, right_halve = arr[:total_len//2], arr[total_len//2:] #get left and right halves or array as seperate arrays
    left_halve = mergesort(left_halve)
    right_halve = mergesort(right_halve)
    return merge_arrays(left_halve, right_halve)

def test_mergesort():
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    print(mergesort(arr))

# quicksort
'''
(1) Take any element as pivot (here, first element)
(2) Divide array into two arrays (without pivot), one array containing elements greater and one array containing lesser than pivot.
(3) Recursively, sort the two arrays so formed.
(4) Finally, merge the 3 arrays together (less_pivot + pivot + more_pivot)
'''
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    arr_without_pivot = arr[:0] + arr[0 +1:]
    less_pivot = []
    more_pivot = []
    for element in arr_without_pivot:
        if element<=pivot:
            less_pivot.append(element)
        else:
            more_pivot.append(element)
    
    less_pivot = quicksort(less_pivot)
    more_pivot = quicksort(more_pivot)


    # merge
    sorted = less_pivot + [pivot] + more_pivot

    return sorted

arr = [7,1,3,5,7,2,3,7,9,10,239,43289473289473298,128937,54983275,4298439]
print(quicksort(arr))
