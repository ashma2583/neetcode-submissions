class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))
            if sort not in dic:
                dic[sort] = [strs[i]]
            elif sort in dic:
                dic[sort].append(strs[i])
        
        output = []
        for s in dic:
            output.append(dic[s])
        return output
