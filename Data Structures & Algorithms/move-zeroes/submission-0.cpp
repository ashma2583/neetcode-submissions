class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i0 = 0;
        int i = 0;
        while (i0 < nums.size()) {
            if (nums[i0] != 0) {
                swap(nums[i], nums[i0]);
                i++;
            }
            i0++;
        }
        return;
    }
};