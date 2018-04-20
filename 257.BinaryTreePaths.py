# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        self.res = []
        path = ""
        self.travel(path,root)
        print(self.res)
        return self.res
    
    def travel(self,path,node):

        if node:
            print(node.val)
            
            if len(path)== 0:
                new_path = str(node.val)
            else:
                new_path = path+"->"+str(node.val)
            if self.last(node):
                print("Found Path"+new_path)
                self.res.append(new_path)
                return
            
            
            if node.left:                
                self.travel(new_path,node.left)
            if node.right:
                self.travel(new_path, node.right)
        return            
        
    def last(self,node):
        if node:
            return (node.left == None and node.right == None)
        return False                
