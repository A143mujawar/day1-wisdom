def perm(s: str):
    ans = []
    a = sorted(s)
    u = [False] * len(a)

    def go(p):
        if len(p) == len(a):
            ans.append("".join(p))
            return
        for i in range(len(a)):
            if u[i]:
                continue
            if i > 0 and a[i] == a[i-1] and not u[i-1]:
                continue
            u[i] = True
            p.append(a[i])
            go(p)
            p.pop()
            u[i] = False

    go([])
    return ans



print(perm("abc"))
