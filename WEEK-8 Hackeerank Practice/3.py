# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        def dfs(node) :
            if not node :
                return 
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        def toListLeft(l) :
            if l :
                return TreeNode(l[0], right=toListLeft(l[1:]))
        return toListLeft(stack)