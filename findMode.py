# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.modes = {}
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.countNode(root)
        print(self.modes)
        if len(self.modes):
            maxVal = max(self.modes.values())
            print("max value",maxVal)
            result = [k for k,v in self.modes.items() if v == maxVal]
            return result
        else:
            return [] 
        
    def countNode(self,root):
        if root:
            if root.val in self.modes:
                self.modes[root.val]+=1
            else:
                self.modes[root.val]=1
                
            self.countNode(root.left)
            self.countNode(root.right)
        
