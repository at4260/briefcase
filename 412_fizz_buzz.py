class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # standard approach, O(1) addl space, O(n) time
		answer = []
        for val in range(1, n + 1):
            # calculate once
            div3 = val % 3 == 0
            div5 = val % 5 == 0
            if div3 and div5:
                answer.append("FizzBuzz")
            elif div3:
                answer.append("Fizz")
            elif div5:
                answer.append("Buzz")
            else:
                answer.append(str(val))

        return answer


        # no modulo usage, O(1) addl space, O(n) time
        # modulo is 2x more computationally expensive than multiplication
        answer = []
        mul3_counter = 1
        mul5_counter = 1
        for val in range(1, n + 1):
            mul3 = 3 * mul3_counter
            mul5 = 5 * mul5_counter
            if val == mul3 and val == mul5:
                answer.append("FizzBuzz")
                mul3_counter += 1
                mul5_counter += 1
            elif val == mul3:
                answer.append("Fizz")
                mul3_counter += 1
            elif val == mul5:
                answer.append("Buzz")
                mul5_counter += 1
            else:
                answer.append(str(val))

        return answer

        # another way, O(1) addl space, O(n) time (precise: 1 + 1/3 + 1/5 + 1/15 = 1 3/5)
        answer = []
        for val in range(1, n+1):
            answer.append(str(val))
        for val in range(3, n+1, 3):
            answer[val - 1] = "Fizz"
        for val in range(5, n+1, 5):
            answer[val - 1] = "Buzz"
        for val in range(15, n+1, 15):
            answer[val - 1] = "FizzBuzz"

        return answer