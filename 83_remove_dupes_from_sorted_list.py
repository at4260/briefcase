# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time, O(1) space
        if not head:
            return head
        p1 = head
        p2 = p1.next 

        while p2:
            if p1.val == p2.val:
                p2 = p2.next
                p1.next = p2
            else:
                p1 = p2
                p2 = p2.next

        return head
    

        # recursive - works from back of list to front
        # O(n) time, O(n) space for recursion stack
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head
    