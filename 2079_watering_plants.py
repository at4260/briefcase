class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # plants = [2,2,3,3], capacity = 5
        # Output: 14
        # river = -1

        # remaining = 5
        # i = 0, plant = 2, remaining = 5-2 = 3, steps = 0- -1 = 1
        # i = 1, plant = 2, remaining = 3-2 = 1, steps = 1- 0 = 1
        # i = 2, plant = 3, remaining = 1-3 <0, steps to river and back = 1--1 = 2  + (-1-2) = 5, remaining = 5-3 = 2, 

        # On time, O1 space
        # steps = 0
        # river = -1
        # prev = -1
        # water_remaining = capacity
        # for i, water_need in enumerate(plants):
        #     # water plant
        #     # count retro steps
        #     # check plant forward + capacity to determine river steps
        #     steps += abs(i - prev)
        #     prev = i
        #     water_remaining -= water_need
 
        #     if i != len(plants) - 1 and water_remaining < plants[i+1]:
        #         # return to the river
        #         steps += abs(i - river) * 2
        #         water_remaining = capacity
                
        # return steps

        steps = 0
        water_remaining = capacity
        for i, water_need in enumerate(plants):
            # water plant
            # count retro steps
            # check plant forward + capacity to determine river steps
            steps += 1
            water_remaining -= water_need
 
            if i != len(plants) - 1 and water_remaining < plants[i+1]:
                # return to the river
                steps += (i+1) * 2
                water_remaining = capacity
                
        return steps

