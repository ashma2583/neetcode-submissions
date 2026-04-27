class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reverse = digits[::-1]
        one, i = 1,0

        while one:
            if i < len(reverse):
                if reverse[i] == 9:
                    reverse[i] = 0
                else:
                    reverse[i] += 1
                    one = 0
            else:
                reverse.append(1)
                one = 0

            i += 1

        return reverse[::-1]
