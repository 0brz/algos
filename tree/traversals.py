class tree:
    def __init__(self, v, left, right):
        self.v = v
        self.left = left
        self.right = right


root = tree(1,
             tree(2,
                   tree(3,
                         tree(4,
                               tree(5, None, None),
                                None),
                            None),
                        None),
                    tree(6, tree(7, tree(8, None, None), tree(9, None, None)), None)
            )

from queue import Queue

def bfs(root: tree):
    print("queue: bfs")
    q = Queue()
    q.put(root)

    while(q.empty() == False):
        sz = q.qsize()
        for i in range(sz):
            cur = q.get()
            print(cur.v)
            if (cur.left != None):
                q.put(cur.left)
            if (cur.right != None):
                q.put(cur.right) 

def dfs(root: tree):
    if (root == None):
        return
    
    print(root.v)

    dfs(root.left)
    dfs(root.right)

def inorder(root: tree):
    if (root == None):
        return
    
    inorder(root.left)
    print(root.v)
    inorder(root.right)

def preorder(root: tree):
    if (root == None):
        return

    print(root.v)
    preorder(root.left)
    preorder(root.right) 

def postorder(root: tree):
    if (root == None):
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.v)

postorder(root)