class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0
        while l < r:
            if height[l] <= height[r]:
                l += 1
                water = maxL - height[l]
                total += water if water > 0 else 0
                maxL = max(height[l], maxL)
            else:
                r -= 1
                water = maxR - height[r]
                total += water if water > 0 else 0
                maxR = max(height[r], maxR)
        return total




