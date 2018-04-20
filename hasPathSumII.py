# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.travel(path,root,sum)
        print(self.res)
        return self.res
    
    def travel(self,path,node,tsum):

        if node:
            print(node.val,tsum)
            new_path = path+ [node.val]
            if self.last(node) and tsum == node.val:
                print("Found Path")
                self.res.append(new_path)
                return
            
            dt = tsum - node.val
            if node.left:                
                self.travel(new_path,node.left,dt)
            if node.right:
                self.travel(new_path, node.right,dt)
        return False            
        
    def last(self,node):
        if node:
            return (node.left == None and node.right == None)
        return False        
