# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:         
        res=[]
        def dfs(node, arr, remaining):
            if not node:
                return 

            arr.append(node.val)
            remaining-=node.val

            if not node.left and not node.right:
                if remaining==0:
                    res.append(arr[:])
                    # return
            else:
                if node.left:
                    dfs(node.left,arr,remaining)
                if node.right:
                    dfs(node.right,arr,remaining)
            arr.pop()
                
        dfs(root, [],targetSum)                
        return res
            


