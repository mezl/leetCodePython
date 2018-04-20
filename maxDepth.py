# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.travel(root,0)
        
    def travel(self,root,level):
        if root:
            print(root.val,level)
            lmax = self.travel(root.left,level+1)
            rmax = self.travel(root.right, level+1)  
            return max(lmax,rmax)
        else:
            return level
