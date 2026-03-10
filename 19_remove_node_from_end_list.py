
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
	
	# two pass approach
	# O(2n) => O(n) time, O(1) space
	counter = 1
	pointer = head
	while pointer.next:
		pointer = pointer.next
		counter += 1

	prev_node_remove = counter - n
	counter = 1
	pointer = head

	# edge case: remove first item in list or if one item in list that's removed
	if prev_node_remove == 0: 
		return pointer.next

	while pointer and pointer.next:
		if counter == prev_node_remove:
			pointer.next = pointer.next.next
			break

		pointer = pointer.next
		counter += 1
	
	return head



	# one pass approach - sliding window
	# use a dummy node to account for edge case of removing one/first item
	# O(n) time, O(1) space
	dummy = ListNode(0, head)
	left = dummy
	right = head

	# initializes fast to be n steps ahead of slow
	for i in range(n - 1):
		right = right.next

	# still considered "one pass" because fast only traverses once
	# this is a continuation of loop before
	while fast.next:
		left = left.next
		right = right.next
	left.next = left.next.next

	return dummy.next

