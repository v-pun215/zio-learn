#mergesort
def mergesort(arr):
    if not arr==[]:
        total_len = len(arr) # get total number of items in list
        left_halve, right_halve = arr[:total_len//2], arr[total_len//2:] #get left and right halves or array as seperate arrays
        print(left_halve, right_halve)


        # --MERGE--
        sorted_array = []
        sorted_array.append(left_halve[0] if left_halve[0]<right_halve[0] else right_halve[0])
        return sorted_array

arr = [5, 10, 15, 20]
print(mergesort(arr))