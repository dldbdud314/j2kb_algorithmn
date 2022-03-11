# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum: int = 0
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs_sum(node):
            if not node:
                return 0
            left = dfs_sum(node.left)
            right = dfs_sum(node.right)
            if node.val < low or node.val > high:
                node.val = 0
            self.sum += node.val #누적합
            return left + right #현 노드 값 = left+right
        dfs_sum(root)
        return self.sum