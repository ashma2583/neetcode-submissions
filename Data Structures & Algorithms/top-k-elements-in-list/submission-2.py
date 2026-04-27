class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
        for num, count in hash.items():
            freq[count].append(num)

        output = []
        for num in freq[::-1]:
            output.extend(num)
            if len(output) == k:
                break

        return output