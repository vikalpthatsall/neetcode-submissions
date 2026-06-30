from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for n, freq in sorted_items[:k]:
                output.append(n)
        return output
                
