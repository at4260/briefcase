import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force - sort and index
        # O(n log n) time, O(1) space

        # max heap
            # time complexity: O(n) heapify + O(k log n) pop k times (two actions) -> O(n + k log n)
            # space complexity: O(n)
        # not great when k = 1 and nums = 1B
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        for i in range(k - 1): # removes the top k - 1 elements, leaving the kth largest element
            heapq.heappop(max_heap)

        res = heapq.heappop(max_heap)
        return -(res)

        # min heap
            # time complexity: O(n) iterate * O(log k) push/pop onto heap k size (loop with inner action) -> O(n log k)
            # space complexity: O(k) for heap k size

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap) # pops smallest off
    
        return min_heap[0]
