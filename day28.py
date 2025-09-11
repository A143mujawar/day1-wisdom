from collections import deque

class Node:
    def _init_(self,v=0,l=None,r=None):
        self.v=v
        self.l=l
        self.r=r

def build(arr):
    if not arr: return None
    root=Node(arr[0])
    q=deque([root])
    i=1
    while q and i<len(arr):
        cur=q.popleft()
        if arr[i] is not None:
            cur.l=Node(arr[i])
            q.append(cur.l)
        i+=1
        if i<len(arr) and arr[i] is not None:
            cur.r=Node(arr[i])
            q.append(cur.r)
        i+=1
    return root

class Sol:
    def isSym(self,root):
        if not root: return True
        def chk(a,b):
            if not a and not b: return True
            if not a or not b: return False
            return a.v==b.v and chk(a.l,b.r) and chk(a.r,b.l)
        return chk(root.l,root.r)


tests=[
    [1,2,2,3,4,4,3],
    [1,2,2,None,3,None,3],
    [1],
    [],
    [1,2,2,3,None,None,3]
]

for t in tests:
    root=build(t)
    print(Sol().isSym(root))
