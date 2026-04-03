# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node:
                return None
            
            # If current node is one of the targets
            if node == p or node == q:
                return node
            
            # Explore left subtree
            left = dfs(node.left)
            # If left returned a true LCA (not just a target), skip right
            if isinstance(left, TreeNode) and left != p and left != q:
                return left
            
            # Explore right subtree
            right = dfs(node.right)
            # If right returned a true LCA (not just a target), skip left
            if isinstance(right, TreeNode) and right != p and right != q:
                return right
            
            # If both sides returned nodes, current node is LCA
            if left and right:
                return node
            
            # Otherwise propagate the non-null side
            return left if left else right
        
        return dfs(root)
