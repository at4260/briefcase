
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
	
	# On time, O1 space
	prev, curr = None, head

	while curr:
		# save next before you lose it
		temp = curr.next
		# flip the pointer around
		curr.next = prev
		# move pointers forward
		prev = curr
		curr = temp

	return prev
	

	# recursive
	# get to the end of the linked list and start repointing from right to left
	# On time - each node gets touched twice (once going down, once coming up) - O(2n)
	# On space - max call depth
		
	# base case - empty list or end of list 
	if not head or not head.next: 
		return head

	new_head = reverseList(head.next)
	head.next.next = head # point the next node's next to yourself
	head.next = None # sever next so that first node is clean and becomes tail

	return new_head # always returning the last node in each call stack   


res = reverseList([1,2,3,4,5])
# output = [5,4,3,2,1]
print('Results: ', res)	
