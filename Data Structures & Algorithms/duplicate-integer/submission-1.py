class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set()
        for n in nums:
            if n in snums:
                return True
            snums.add(n)
        return False