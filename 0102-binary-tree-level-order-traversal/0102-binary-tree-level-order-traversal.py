# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]

        q=collections.deque()
        q.append(root)

        while q:
            level=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp:
                    level.append(temp.val)
                    q.append(temp.left)
                    q.append(temp.right)
            if level:
                res.append(level)
        
        return res
                

        