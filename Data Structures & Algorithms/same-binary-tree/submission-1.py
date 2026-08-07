class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        leftP = self.isSameTree(p.left, q.left)
        rightP = self.isSameTree(p.right, q.right)

        if ((p.val == q.val) and leftP and rightP):
            return True
        else:
            return False