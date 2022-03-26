class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if val == root.val:
            return root
        return self.searchBST(root.left if val < root.val else root.right, val)

