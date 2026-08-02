class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getArea(i, j): 
            return min(heights[i], heights[j]) * (j - i)
        max_area = 0
        i = 0
        j = len(heights) - 1
        while (i < j):
            area = getArea(i, j)
            if (area > max_area):
                max_area = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area