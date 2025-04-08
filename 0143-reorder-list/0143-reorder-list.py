# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head and not head.next:
            return
        slow, fast=head, head.next

        while fast and fast.next: 
            slow=slow.next
            fast=fast.next.next
        
        temp_head=slow.next
        slow.next=None
        new_head=self.reverse_list(temp_head)

        curr1,curr2=head, new_head

        while curr1 and curr2:
            temp1=curr1.next
            temp2=curr2.next

            curr1.next=curr2
            curr2.next=temp1

            curr1=temp1
            curr2=temp2

    
    def reverse_list(self, head):
        curr, prev=head, None

        while curr:
            nxt= curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        