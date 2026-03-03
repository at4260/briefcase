def carFleet(target: int, position: List[int], speed: List[int]) -> int:

	# monotonic stacks solution (sorted array where there's a need to efficiently track 
	# unresolved items where the most recent one is always next to resolve)
	# Onlogn time (due to sorting, otherwise On), On space

	# sort position and speed arrays together by order of closest to target
	pairs = sorted(zip(position, speed), reverse = True)
	ttd = [ (target - pair[0]) / pair[1] for pair in pairs ]

	stack = []
	for t in ttd:
		if stack and stack[-1] >= t:
			continue # move onto next loop; alt is `if not stack or stack[-1] < t`
		stack.append(t)

	return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
# output 3
res = carFleet(target, position, speed)
print('Results: ', res)	
