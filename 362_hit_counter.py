# Design a Hit Counter (LC #362)
# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).
# Your system should accept a timestamp (in seconds) and support two functions:

# hit(timestamp) — records a hit at the given timestamp
# getHits(timestamp) — returns the number of hits in the past 300 seconds from the given timestamp (inclusive)

# Note: Timestamps are called in non-decreasing order (you can assume hits always come in chronological order).


from collections import deque


hit_queue = deque()

def hit(timestamp: int):
    hit_queue.append(timestamp)

def getHits(timestamp: int) -> int:
    start_time = max(0, timestamp - 300) 

    while hit_queue:
        hit = hit_queue.popleft()
        if hit > start_time:
            return len(hit_queue) + 1

    return 0




class HitCounter:
    def __init__(self):
        self.hit_queue = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        start_time = max(0, timestamp - 299)
        
        while self.hit_queue:
            if self.hit_queue[0] < start_time:
                self.hit_queue.popleft()
            else:
                break
        
        return len(self.hit_queue)