# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        
        def isSametree(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return isSametree(a.left, b.left) and isSametree(a.right, b.right)
            else:
                return False
        
        if isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)