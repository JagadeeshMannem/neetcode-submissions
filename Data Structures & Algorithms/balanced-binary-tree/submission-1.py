# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = 0
        if root != None:
            leftLen = self.maxDepth(root.left)
            rightLen = self.maxDepth(root.right)
            length += max(leftLen, rightLen) + 1
        return length

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        isBalanced = False

        hLeft = self.maxDepth(root.left)
        hRight = self.maxDepth(root.right)

        return abs(hLeft - hRight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)