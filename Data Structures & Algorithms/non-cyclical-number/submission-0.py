class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            sum_of_squares = 0
            s = str(n)
            for i in s:
                integer = int(i)
                sum_of_squares += integer ** 2
            if sum_of_squares in visited:
                return False
            else:
                n = sum_of_squares
                visited.add(n)
        return True


