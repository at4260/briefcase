
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

	# O(n+m) -> O(n) time, O(1) space
	dummy = ListNode(0)
	curr = dummy

	while list1 and list2:
		if list1.val <= list2.val:
			curr.next = list1
			list1 = list1.next
		else:
			curr.next = list2
			list2 = list2.next
		curr = curr.next

	# finish tying things up
	curr.next = list2 if list1 is None else list1

	return dummy.next


	# recursive - O(n+m) -> O(n) time, O(n+m) space due to call stack depth
	# base case
	if list1 is None:
		return list2
	if list2 is None:
		return list1

	if list1.val <= list2.val:
		next_node = self.mergeTwoLists(list1.next, list2)
		list1.next = next_node
		return list1
	else:
		next_node = self.mergeTwoLists(list1, list2.next)
		list2.next = next_node
		return list2
	

list1 = [1,2,4]
list2 = [1,3,4]
# output = [1,1,2,3,4,4]
res = mergeTwoLists(list1, list2)
print('Results: ', res)	
