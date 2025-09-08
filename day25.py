class Node:
    def _init_(self, v):
        self.v = v
        self.l = None
        self.r = None

class Sol:
    def isBST(self, root):
        def chk(n, low, high):
            if not n: return True
            if not (low < n.v < high): return False
            return chk(n.l, low, n.v) and chk(n.r, n.v, high)
        return chk(root, float("-inf"), float("inf"))

if _name_ == "_main_":
    r1 = Node(2)
    r1.l = Node(1)
    r1.r = Node(3)
    print(Sol().isBST(r1))
