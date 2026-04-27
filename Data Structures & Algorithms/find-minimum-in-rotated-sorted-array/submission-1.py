class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                output = min(nums[l], output)
                break
            
            mid = (l + r) // 2
            output = min(nums[mid], output)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return output