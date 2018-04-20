# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.travel(root.left,root.right)
        return True
        
    def travel(self,left,right):
        if left is None and right is None:
            return True
        
        if left and right and left.val == right.val:
                       
            ll = self.travel(left.left,right.right)
            rr = self.travel(left.right,right.left)  
            return (ll and rr)
        else:
            return False
        
