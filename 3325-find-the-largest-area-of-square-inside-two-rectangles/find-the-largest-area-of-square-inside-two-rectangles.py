class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            x1_i, y1_i = bottomLeft[i]
            x2_i, y2_i = topRight[i]

            for j in range(i + 1, n):
                x1_j, y1_j = bottomLeft[j]
                x2_j, y2_j = topRight[j]

                # Intersection coordinates
                left = max(x1_i, x1_j)
                right = min(x2_i, x2_j)
                bottom = max(y1_i, y1_j)
                top = min(y2_i, y2_j)

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)

        return max_area
