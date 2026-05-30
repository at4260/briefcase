
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list) # { "key1": [(5, "val1"), (10, "val2"), (20, "val3") ] }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    # def get(self, key, timestamp) -> str:
    #     # O(n) time
    #     if key not in self.store:
    #         return ""
        
    #     data = self.store[key]
    #     if data: 
    #         for i in range(len(data)-1, -1, -1): # loop backwards
    #             if data[i][0] <= timestamp:
    #                 return data[i][1]
                     
    #     return ""

    def get(self, key, timestamp) -> str:
        # binary search - O(log n)
        if key not in self.store:
            return ""
        
        data = self.store[key]
        if not data: 
            return ""
        
        if timestamp < data[0][0]:
            return ""
        left = 0
        right = len(data) - 1
        while left <= right: # check
            mid = (left + right) // 2
            if data[mid][0] == timestamp:
                return data[mid][1]
            elif data[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return data[left - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
