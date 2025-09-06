from collections import deque

def swm(arr, k):
    n = len(arr)
    if n * k == 0:
        return []
    if k == 1:
        return arr
    q = deque()
    res = []
    for i in range(n):
        if q and q[0] == i - k:
            q.popleft()
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(arr[q[0]])
    return res

print(swm([1, 3, -1, -3, 5, 3, 6, 7], 3))
