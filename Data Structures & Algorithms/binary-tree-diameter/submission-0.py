class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            lheight = height(node.left)
            rheight = height(node.right)

            diameter = max(diameter, lheight + rheight)

            return max(lheight, rheight) + 1

        height(root)
        return diameter