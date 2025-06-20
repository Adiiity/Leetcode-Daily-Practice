"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        copyMap={None:None}
        curr=head

        while curr:
            copy=Node(curr.val)
            copyMap[curr]=copy
            curr=curr.next

        curr=head
        while curr:
            copy=copyMap[curr]
            copy.next=copyMap[curr.next]
            copy.random=copyMap[curr.random]
            curr=curr.next
        
        return copyMap[head]
        