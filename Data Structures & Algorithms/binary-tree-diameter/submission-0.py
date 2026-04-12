# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def long(r):
            nonlocal ans
            if r is None:
                return 0
            left = long(r.left)
            right = long(r.right)
            ma = max(left, right) + 1
            ans = max(ans, left + right)
            return ma
        long(root)
        return ans
            
        