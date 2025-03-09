class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        result = len(points)
        i = 0
        while i < len(points) - 1:
            if points[i][1] >= points[i + 1][0]:
                result -= 1
                points[i + 1][1] = min(points[i + 1][1], points[i][1])

            i += 1
        return result