class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity=0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                capacity = min(heights[i],heights[j]) * (j-i)
                maxCapacity = max(maxCapacity, capacity)

        return maxCapacity
        