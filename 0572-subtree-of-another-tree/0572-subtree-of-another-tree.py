# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
       
        if not t:
            return True
        if not s:
            return False

        if self.isSameTree(s,t):
            return True
        else:
            return (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))

    def isSameTree(self,s,t):
        if not s and not t:
            return True
        
        if s and t and s.val==t.val:
            return (self.isSameTree(s.left, t.left) and 
                    self.isSameTree(s.right,t.right))
        else:
            return False
