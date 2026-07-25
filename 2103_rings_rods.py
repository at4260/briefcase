class Solution:
    def countPoints(self, rings: str) -> int:

        # rings = "B0B6G0R6R0R6G9"
        # odd index = position
        # even index = color
        # {0: {B, G, R}, 6: {B, R}, 9: {G}}
        # must have RGB, not just len 3

        # On time, On space
        locations = defaultdict(set)
        for i, ring in enumerate(rings):
            if i % 2 == 1: # odd index = position
                locations[ring].add(rings[i - 1])

        return sum(1 for rod_set in locations.values() if len(rod_set) == 3)
