# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maximum):
            if root is None:
                return 0

            count = 0

            if maximum is None or root.val >= maximum:
                count = 1

            maximum = root.val if maximum is None else max(maximum, root.val)

            count += dfs(root.left, maximum)
            count += dfs(root.right, maximum)

            return count

        return dfs(root, None)
        
        