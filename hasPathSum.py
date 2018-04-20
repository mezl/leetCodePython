# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.found = False
        self.travel(root,sum)
        return self.found
    
    def travel(self,node,tsum):

        if self.found:
            return True
        if node:
            print(node.val,tsum)
            if self.last(node) and tsum == node.val:
                print("Found Path")
                self.found = True
                return True
            
            dt = tsum - node.val
            if node.left:                
                self.travel(node.left,dt)
            if node.right:
                self.travel(node.right,dt)
        return False            
        
    def last(self,node):
        if node:
            return (node.left == None and node.right == None)
        return False
