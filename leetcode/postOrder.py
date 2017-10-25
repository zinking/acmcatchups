# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r = []
        nds = []
        if root is None: return r
        nds.append(root)
        import pdb
        #pdb.set_trace()
        while len(nds) > 0 :
            nd = nds[-1]
            re = nd.right is None
            le = nd.left is None
            hasR = len(r)>0
            isLeaf = le and re
            isLRVisited = (not le and not re and hasR and r[-1] == nd.right.val)
            isLVisited = (not le and hasR and r[-1] == nd.left.val)
            isRVisited = (not re and hasR and r[-1] == nd.right.val)
            if isLeaf or isLRVisited or isLVisited or isRVisited:
                nd = nds.pop()
                print nd.val
                print r
                r.append(nd.val)
            else:
                if not re:nds.append(nd.right)
                if not le:nds.append(nd.left)

        return r


solver = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n2.left = n3

print solver.postorderTraversal(None)
print solver.postorderTraversal(n1)

