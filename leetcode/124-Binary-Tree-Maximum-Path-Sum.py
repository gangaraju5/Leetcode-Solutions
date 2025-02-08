# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximumpath=[float('-inf')]
        self.pathsum(root,maximumpath)
        return maximumpath[0]
    def pathsum(self,root: Optional[TreeNode],maximumpath) -> int:
        if root is None:
            return 0
        left=max(0,self.pathsum(root.left,maximumpath))
        right =max(0,self.pathsum(root.right,maximumpath))
        maximumpath[0]= max(maximumpath[0],root.val+left+right)
        return root.val+ max(left,right)
        