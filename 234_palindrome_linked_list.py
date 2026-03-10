# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(2n) => O(n) time, O(n) space
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        left = 0
        right = len(vals) - 1
        while left <= right: #check
            if vals[left] != vals[right]:
                return False
            left +=1
            right -= 1

        return True        

        # O(3 * n/2) -> O(n) time, O(1) space
        slow = head
        fast = head

        # get slow to the middle
        # in odd len list - middle is true middle
        # in even len list - middle is left-middle
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the right half of the list
        pointer = slow.next
        slow.next = None
        while pointer:
            tmp = pointer.next
            pointer.next = slow
            slow = pointer
            pointer = tmp

        # slow is at the end; compare against head
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True    
