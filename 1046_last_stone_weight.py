class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force - sorting
        # O(n^2 log n) time, O(1) addl space
        # while len(stones) > 1:
        #     stones.sort()
        #     largest = stones.pop()
        #     next_largest = stones.pop()
        #     new_stone = largest - next_largest
        #     stones.append(new_stone)

        # return stones[0]

        # max heap to store largest values
        # O(n log n) time, O(n) space
        import heapq

        max_heap = [-s for s in stones] # to support max heap
        heapq.heapify(max_heap)
        # [-8, -7, -4, -2, -1, -1]

        while len(max_heap) > 1:
            largest = -(heapq.heappop(max_heap)) # convert back to positive, skip abs() in case it's a neg original val
            next_largest = -(heapq.heappop(max_heap)) # convert back to positive
            new_stone = largest - next_largest
            heapq.heappush(max_heap, -new_stone) # insert back as neg for max heap

        return -(max_heap[0]) # convert back to positive
