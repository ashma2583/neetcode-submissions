class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mlow, mhigh = 0, len(matrix) -1
        nlow, nhigh = 0, len(matrix[0]) - 1

        while mhigh >= mlow:
            midrow = (mhigh + mlow) // 2
            if target > matrix[midrow][-1]:
                mlow = midrow + 1
            elif target < matrix[midrow][0]:
                mhigh = midrow - 1
            else:
                break
        
        if not (mhigh >= mlow):
            return False
        midrow = (mhigh + mlow) // 2
        while nhigh >= nlow:
            mid = (nlow + nhigh) // 2
            if target == matrix[midrow][mid]:
                return True
            elif target < matrix[midrow][mid]:
                nhigh = mid - 1
            elif target > matrix[midrow][mid]:
                nlow = mid + 1
                
        return False
