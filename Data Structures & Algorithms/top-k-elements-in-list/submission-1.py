class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            elif num in dic:
                dic[num] += 1
        
        arr = []
        for n, count in dic.items():
            arr.append([count, n])
        arr.sort()

        output = []
        while len(output)<k:
            output.append(arr.pop()[1])
        
        return output