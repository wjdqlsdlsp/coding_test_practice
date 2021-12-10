import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.parent = None
        self.data = None
        self.index = None
    
def preOrder(root, vector):
    if root == None:
        return vector
    
    vector.append(root.index)
    preOrder(root.left, vector)
    preOrder(root.right, vector)
    return vector

def postOrder(root, vector):
    if root == None:
        return vector
    
    postOrder(root.left, vector)
    postOrder(root.right, vector)
    vector.append(root.index)
    return vector
    

def solution(nodeinfo):
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i] += [i+1] 
    nodeinfo = sorted(nodeinfo, key= lambda x : x[1], reverse=True)
    root = None
    for i, node in enumerate(nodeinfo):
        new = Node()
        new.index = node[2]
        new.data = node
        if root == None:
            root = new
        else:
            cur = root
            while True:
                if cur.data[0] < new.data[0]:
                    if cur.right == None:
                        cur.right = new
                        new.parent = cur
                        break
                    else:
                        cur = cur.right
                else:
                    if cur.left == None:
                        cur.left = new
                        new.parent = cur
                        break
                    else:
                        cur = cur.left
    return [preOrder(root, []), postOrder(root, [])]