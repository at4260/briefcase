# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # O(m+n) time, O(1) space
        carry = 0
        new = ListNode(0)
        newp = new

        # while l1 or l2:
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry

            # if total > 9:
            #     carry = 1 # total // 10 => always 1
            #     right_digit = total % 10
            #     newp.next = ListNode(right_digit)
            # else:
            #     carry = 0
            #     newp.next = ListNode(total)
            carry = total // 10 # equals 1 or 0
            new_val = total % 10
            newp.next = ListNode(new_val)

            newp = newp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # ending case
        # if carry == 1:
        #     newp.next = ListNode(1)

        return new.next


