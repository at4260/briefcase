
def generateParenthesis(n: int) -> List[str]:
	# simplified
		# time - O(2^n) (exponential, tree with size 2 (max 2 options each node) at each 2n position)
		# space - O(2n) (max recurisve calls is 2n/most number of layers is 2n to generate each parens)=> O(n)
	# technically
		# time - O(4^n / √n) - Catalan number formula
		# space - O(2n) => O(n)
	res = []

	# recursive
	# when branching at a node, it'll go 
	# 	universe 1 - finishes all the way through to the end
	#	comes back and finishes universe 2 node
	# note: need to send in vars vs setting it and then passing into the func
	# due to the mutated vars from universe 1 getting used in universe 2
	def backtrack(strr, openC, closeC):
		if openC == 0 and closeC == 0: # finished
			res.append(strr)
			return
		if openC != 0: # universe 1
			backtrack(strr + "(", openC - 1, closeC)
		if closeC > openC: # universe 2
			backtrack(strr + ")", openC, closeC - 1)

	strr = ""
	backtrack(strr, openC = n, closeC = n)

	return res

s = 3
# output = ["((()))","(()())","(())()","()(())","()()()"]
res = generateParenthesis(s)
print('Results: ', res)	
