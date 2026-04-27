class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = {}
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)
        if len(nums) == 0:
            return 0
        for num in nums:
            if (num-1) in sequence.keys():
                sequence[num-1] += 1
                seq = sequence.pop(num-1)
                sequence[num] = seq
            else:
                sequence[num] = 1
            print(sequence)
        
        return max(sequence.values())

        