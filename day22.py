def first_element_k_times(arr, k):
    freq = {}

     
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

     
    for num in arr:
        if freq[num] == k:
            return num

    return -1


 
arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(first_element_k_times(arr, k))
