class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # brute force
        # compare arr1 across arr2 is O(n*m) where n = arr1 len, m = arr2 len

        res = 0
        for val1 in arr1:
            is_valid = True
            for val2 in arr2:
                if abs(val1 - val2) <= d:
                    is_valid = False
                    break
                    
            if is_valid:
                res += 1

        return res

        # optimal - sort + binary search
        # O(m log m) + (O(log m) * O(n)) = O((n+m) log m time where n = len(arr1), m = len(arr2)
        # O(m) space for sorted arr2
        # [4,5,8] [1,8,9,10]
        # 4 - (2,6)
        # 5 - (3,7)
        # 8 - (6,10)

        #  arr1 = [2,1,100,3], arr2 = [-5,-3,-2,7,10], d = 6
        #  2 => (-4,8)
        #  1 => (-5,7)
        #  100 => (94,106)
        #  3 => (-3,9)

        counter = 0
        sorted_arr2 = sorted(arr2)
        for val in arr1:
            min_val_valid = True
            min_val, max_val = val - d, val + d
            # binary search on sorted_arr2 against min_val
            left, right = 0, len(sorted_arr2) - 1
            # while left <= right:
            #     mid = (left + right) // 2
            #     if sorted_arr2[mid] == min_val:
            #         min_val_valid = False
            #         break
            #     elif sorted_arr2[mid] < min_val:
            #         left = mid + 1
            #     else: # sorted_arr2[mid] > min_val:
            #         right = mid - 1

            # # left represents the insertion point
            # max_val_valid = (left > len(sorted_arr2) - 1) or (max_val < sorted_arr2[left])
            # if min_val_valid and max_val_valid:
            #     counter += 1

            while left <= right:
                mid = (left + right) // 2
                if sorted_arr2[mid] < min_val:
                    left = mid + 1
                else:
                    right = mid - 1

            # left represents the insertion point
            if left > len(sorted_arr2) - 1) or (max_val < sorted_arr2[left]):
                counter += 1            

        return counter


