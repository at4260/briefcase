def hasCycle(head: Optional[ListNode]) -> bool:
	# O(n) time, space
	seen = set(head)
	curr = head
	
	while curr:
		if curr in seen:
			return True
		seen.add(curr)
		curr = curr.next

	return False

	# fast slow pointer 
	# Floyd's cycle detection algo says two pointers with one going
	# at 1, one going at 2, will always eventually meet
	# o(n) time, o(1) space
	fast = head
	slow = head

	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return True            
	return False


head = [3,2,0,-4], pos = 1
# output = true
res = hasCycle(head)
print('Results: ', res)	
