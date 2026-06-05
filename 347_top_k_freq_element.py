class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import defaultdict

        # hash map + max heap
        # time complexity
            # O(n) for map creation + O(n) for heapify + O(k log n) for the popping -> O(n + k log n)
        # space complexity 
            # O(n) for map + O(n) for heap -> O(n) space
        # more efficient than min heap if k is closer to n

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1 # {value: count}
        
        max_heap = [(-v, k) for k, v in seen.items()] 
        heapq.heapify(max_heap) 

        # seen = [(-3,1), (-2,2), (-1,3)]  tuple (count , value) 

        res = []
        for i in range(k):
            largest = heapq.heappop(max_heap)[1]
            res.append(largest)

        return res


        # hash map + min heap
        # time complexity
            # O(n) for map creation + O(n) for loop * O(log k) for the popping -> O(n log k)
        # space complexity 
            # O(n) for map + O(k) for heap -> O(n) space

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1 # {value: count}
        # seen = {1: 3, 2:2, 3: 1}

        min_heap = []
        for key, val in seen.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
    
        # results don't need to be ordered but if they did, max heap would be a better solution since we just pop naturally from
        # largest to smallest; min heap here would need to reverse the elements in the list since we're ordered small to large
        return [tup[1] for tup in min_heap]

