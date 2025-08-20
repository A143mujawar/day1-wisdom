def day6(arr):
    result = []
    prefix_sum = 0
    hashmap = {0: [-1]}  

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        hashmap.setdefault(prefix_sum, []).append(i)

    return result



arr = [1, 2, -3, 3, -1, 2]
print(day6(arr))
