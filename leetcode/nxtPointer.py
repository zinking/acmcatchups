class Node(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        def getNextSibling(node):
            if node is None: return None
            if node.left is not None: return node.left
            elif node.right is not None: return node.right
            elif node.next is not None: return getNextSibling(node.next)
            return None
            
        def connectlr(node, nxtSib):
            if node is None: return
            
            node.next = nxtSib
            if node.left is None and node.right is None:return
            
            nnxtSib = getNextSibling(node.next)
            print 'sibling of ',node.val, ' is ', nnxtSib.val if nnxtSib is not None else None
            if node.left is not None and node.right is not None:
                connectlr(node.right, nnxtSib)
                connectlr(node.left, node.right)
            elif node.left is None:
                connectlr(node.right, nnxtSib)
            elif node.right is None:
                connectlr(node.left, nnxtSib)
                
        connectlr(root,None)


solver = Solution()
nodes = map(lambda x:Node(x), range(10))
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
#nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
nodes[3].left = nodes[7]
nodes[6].right = nodes[8]

solver.connect(nodes[0])
nodes[0].next = nodes[1]
nodes[2].next = nodes[3]
nodes[6].next = nodes[7]

p = nodes[0]
s = ""
while p is not None:
    s += str(p.val) + " -> "
    p = p.next

print s



