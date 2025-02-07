# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum=[0]
        self.height(root,maximum)
        return maximum[0]
              
    def height(self,root: Optional[TreeNode],maximum) -> int:
        if root is None:
            return 0
        lh=self.height(root.left,maximum)
        rh=self.height(root.right,maximum)
        maximum[0]=max(maximum[0],lh+rh)
        return 1+ max(lh,rh)
        
        