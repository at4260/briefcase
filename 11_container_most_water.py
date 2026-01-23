

def maxArea(height: list) -> int:
    # brute force
    # On2 time, O1 space
    # area = 0
    # for i in range(len(height)):
    #     for j in range(i + 1, len(height)):
    #         min_height = min(height[i], height[j])
    #         width = j - i
    #         area = max(min_height * width, area)

    # return area

    # ideal
    # on time, o1 space
    area = 0
    left, right = 0, len(height) - 1
    while left < right:
        min_height = min(height[left], height[right])
        width = right - left
        area = max(min_height * width, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        # more efficient to add this clause to move both pointers inwards
        # since we know that there aren't any better possibilities by
        # moving either pointers inwards, so might as well move both
        # [2,8,10,1,8] => (1,2) and (1,3) will never be > than (1,4)
        # likewise (2,4) and (3,4) will never be > than (1,4)
        # so move left and right both in so we can check (2,3)
        # elif height[left] == height[right]:
        #     left += 1
        #     right -= 1

    return area


height = [1,8,6,2,5,4,8,3,7]	
res = maxArea(height)
print('Results: ', res)	
