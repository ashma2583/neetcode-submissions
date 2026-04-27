class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hash;
        for (int num : nums) {
            if (hash.count(num)) {
                return true;
            }
            hash.insert(num);
        }
        return false;
    }
};