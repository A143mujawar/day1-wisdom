arr = [16, 17, 4, 3, 5, 2]
ans = []
n = len(arr)
maxr = arr[-1]
ans.append(maxr)

for i in range(n-2, -1, -1):
    if arr[i] > maxr:
        maxr = arr[i]
        ans.append(maxr)

ans.reverse()
print("Leaders:", ans)
