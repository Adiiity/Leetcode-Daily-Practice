# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        curSum=0
        def dfs(node,num):
            nonlocal curSum
            if not node:
                return
            
            # strNum+=str(node.val)
            num=num*10+node.val
            if not node.left and not node.right:
                curSum+=num
            
            if node.left:
                dfs(node.left,num)
            if node.right:
                dfs(node.right,num)
            
            
        dfs(root,0)
        return curSum

        