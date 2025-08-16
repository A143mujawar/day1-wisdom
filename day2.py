def day2(arr): 
    n = len(arr) + 1
    total = n * (n + 1) //2

    sum_val = 0
    for num in arr:
        sum_val += num

    return total - sum_val


arr = [1, 2, 4, 5]
print(day(arr))
