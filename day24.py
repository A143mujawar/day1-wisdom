class Node:
    def _init_(self, v):
        self.v = v
        self.l = None
        self.r = None

class Sol:
    def lca(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lca(root.l, p, q)
        right = self.lca(root.r, p, q)
        if left and right:
            return root
        return left if left else right

if _name_ == "_main_":
    root = Node(3)
    root.l = Node(5)
    root.r = Node(1)
    root.l.l = Node(6)
    root.l.r = Node(2)
    root.r.l = Node(0)
    root.r.r = Node(8)
    root.l.r.l = Node(7)
    root.l.r.r = Node(4)

    s = Sol()
    p = root.l
    q = root.l.r.r
    print(s.lca(root, p, q).v)
