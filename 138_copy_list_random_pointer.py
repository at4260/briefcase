# REVIEW

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(2n) -> O(n) time, O(n) space
        # copy the first node, hold on next and random
        dummy = Node(0)
        og_pointer = head # pointer
        new_pointer = dummy
        old_to_new = {} # old node: new node

        # first pass - creates the copy LL with val and next
        # while saving the random node
        while og_pointer:
            new_pointer.next = Node(og_pointer.val)
            new_pointer = new_pointer.next
            old_to_new[og_pointer] = new_pointer
            og_pointer = og_pointer.next

        # second pass - traverse new LL and link up random
        og_pointer = head # reset
        new_pointer = dummy.next # reset
        while new_pointer:
            new_pointer.random = old_to_new[og_pointer.random] if og_pointer.random else None
            og_pointer = og_pointer.next
            new_pointer = new_pointer.next
            

        return dummy.next


        # O(n) time, O(n) space
        # copy the first node, hold on next and random
        og_pointer = head # pointer
        dummy = Node(0)
        new_pointer = dummy
        old_to_new = {None: None} # old node: new node

        while og_pointer:
            # lookup to connect to existing node or create new node
            if og_pointer in old_to_new:
                new_pointer.next = old_to_new[og_pointer]
            else:
                new_pointer.next = Node(og_pointer.val)
                old_to_new[og_pointer] = new_pointer.next
            new_pointer = new_pointer.next

            if og_pointer.random in old_to_new:
                # make the .random link
                new_pointer.random = old_to_new[og_pointer.random]
            else:
                # create the node
                new_random_node = Node(og_pointer.random.val) # None already handled above
                old_to_new[og_pointer.random] = new_random_node
                new_pointer.random = new_random_node
            og_pointer = og_pointer.next

        return dummy.next
