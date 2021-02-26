# Binary Search Tree Operations


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def root(T):
    while T.parent != None:
        T = T.parent
    return T

def search(T,k):
    if T == None or T.value == k:
        return T
    
    if T.value < k: # if the value of the parent is 
        # less than the key, we want to go right of the
        # tree
        return search(T.right, k)
    else: return search(T.right, k)

def insert(T, k): # where T is the root
    y = None
    x = T
    z = Node(k)
    while x != None:
        y = x
        if z.value < x.value:
            x = x.left
        else: x = x.right
    z.parent = y
    if y == None:
        T = z
    else:
        if z.value < y.value:
            y.left = z
        else: y.right = z
    return T

def inordertreewalk(x):
    if x != None:
        inordertreewalk(x.left)
        print(x.value)
        inordertreewalk(x.right)

def treemin(x):
    while x.left != None:
        x = x.left
    return x

def treemax(x):
    while x.right != None:
        x = x.right
    return x

def treesuccessor(T, x):
    x = search(T, x)
    y = None
    if x == None:
        return None
    if x.right != None:
        return treemin(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y
        y = y.parent
    return y

def treedelete(T, x):
    x = search(T, x)
    z = x

    if z.left or z.right == None:
        y = z
        return root(y)
    else: y = treesuccessor(T, z)
    if y.left != None:
        x = y.left
    else: x = y.right
    if x != None:
        x.parent = y.parent
    if y.parent == None:
        # deleted the only node so build it
        return y # unsure if this is right
    else:
        if y == y.parent.left:
            y.parent.left = x
        else: y.parent.right = x
    if y != z:
        z.value = y.value
    return root(y)

r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
print(r.value)
print(r.right.value)
r = insert(r, 80)
r = treedelete(r, 80)
print(root(r).value)
inordertreewalk(r)
