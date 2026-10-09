class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                areas.append(area)
        return max(areas)