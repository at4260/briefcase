class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # brute force - O(n*m) n = high - low values, m = num of digits per n, O1 excluding output array
        # def is_sequential(num):
        #     str_num = str(num)
        #     for i in range(1, len(str_num)):
        #         if int(str_num[i-1]) + 1 != int(str_num[i]):
        #             return False
        #     return True

        # res = []
        # for num in range(low, high + 1):
        #     if is_sequential(num):
        #         res.append(num)
         
        # return res


        # ideal solution is to generate numbers
        # but result set is not sorted
        # O(9*9)-> O(1) time, O(1) space excluding output array
        # res = []
        # for i in range(1,10): # digits 1-9
        #     num, iterator = i, i
        #     while num <= high:
        #         if num >= low:
        #             res.append(num)
        #         if iterator >= 9:
        #             break
        #         iterator += 1
        #         num = (num * 10) + (iterator)
                
        # return res


        # low = 100, high = 300
        # return sorted results after checking each value
            # len = 1 => 1,2,3...,9
            # len = 2 => 12,23,34,...89
            # len = 3 => 123,234,345,...789
        # O(9*9*8)-> O(1) time, O(1) space excluding output array
        res = []
        for length in range(1,10): # length of num

            for start in range(1,10): # digits 1-9
                num = start
                if num > (9-length + 1):
                    break
                for i in range(length - 1):
                    num = (num * 10) + ((num % 10) + 1)

                if low <= num <= high:
                    res.append(num)
            
        return res


              