# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arry = []
        self.travel(root,0,arry)
        return (arry)
    def travel(self,root,level,array):
        if root:
            print(root.val,level)
            #check level array exist or not
            try:
                array[level]
            except:
                array.append([])
                
            array[level].append(root.val)
            self.travel(root.left,level+1,array)
            self.travel(root.right, level+1,array)        
