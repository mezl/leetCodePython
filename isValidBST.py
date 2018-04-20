# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys

        mmin = -sys.maxsize-1
        mmax = sys.maxsize
        return self.minmax(root,mmin,mmax)

    def minmax(self,root,mmin,mmax):
        if root:
            if root.val > mmin and root.val < mmax:
                L = self.minmax(root.left,mmin,root.val)
                R = self.minmax(root.right,root.val,mmax)
                return L and R
            else:
                return False
        else:
            return True
        
        
        

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
s = Solution()
print(s.isValidBST(root))

