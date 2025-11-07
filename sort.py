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
    print("left:",left_halve,"+ right:", right_halve)
    left_halve = mergesort(left_halve)
    right_halve = mergesort(right_halve)
    return merge_arrays(left_halve, right_halve)

def test_mergesort():
    arr = [10,9,8,7,6,5,4,3,2,1,0]
    print(mergesort(arr))

# quicksort
