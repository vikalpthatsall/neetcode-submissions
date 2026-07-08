class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for current in nums:
            if current-1 not in nums:
                length  = 0
                while current + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest