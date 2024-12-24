# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val==1
        
        leftResult=self.evaluateTree(root.left)
        rightResult=self.evaluateTree(root.right)
        if root.val==2:
            return leftResult or rightResult
        if root.val==3:
            return leftResult and rightResult
        
        
        