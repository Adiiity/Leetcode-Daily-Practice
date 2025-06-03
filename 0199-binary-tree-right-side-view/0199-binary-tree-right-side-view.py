# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            rightSide=None
            for i in range(len(q)):
                right_temp=q.popleft()
                if right_temp:
                    rightSide=right_temp
                    q.append(right_temp.left)
                    q.append(right_temp.right)
            if rightSide:
                res.append(rightSide.val)
        return res
                