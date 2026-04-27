class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "-" + s
        return output

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        output = []
        i=0
        while i < len(s):
            j = i + 1
            while s[j] != '-':
                j += 1
            word_count = int(s[i:j])
            output.append(s[j+1: j+1+word_count])
            i = j+1+word_count
        return output


