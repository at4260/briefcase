# REVIEW

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # O(3*n/2) => O(n) time, O(1) space
        # fast/slow pointers to get to the middle and end of LL
        fast, slow = head, head
        # odd len - true middle; even len - left of middle
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # use slow pointer to reverse right half of LL
        # don't let right half reverse back into the left half
        # ex: in [1,2,3,4] -> [1,2] and [4,3] not [4,3,2] which causes a 
        # bug in the relink later
        
        # sever middle node's link
        mid = slow         
        slow = slow.next   
        mid.next = None
        # sever next node's link back to the middle
        prev = None

        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            

        # relink using head and end pointers while moving inwards
        left = head
        right = prev
        while left and right:
            tmp_left = left.next
            left.next = right
            left = tmp_left
            
            tmp_right = right.next
            right.next = left
            right = tmp_right

