class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurance = set()

        for num in nums:
            if num in occurance:
                return True
            occurance.add(num)

        return False
