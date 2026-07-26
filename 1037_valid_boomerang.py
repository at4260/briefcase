class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # compare slopes between points
            # By-Ay/Bx-Ax = Cy-By/Cx-Bx
            # but this risks divide by 0
        # reformat to cross multiple
            # By-Ay * Cx-Bx = Cy-By * Bx-Ax

        # O(1) time, space due to 3 points
        point_set = set([tuple(point) for point in points])
        if len(point_set) != 3:
            return False

        cross1 = (points[1][1] - points[0][1]) * (points[2][0] - points[1][0])
        cross2 = (points[2][1] - points[1][1]) * (points[1][0] - points[0][0])

        return cross1 != cross2
