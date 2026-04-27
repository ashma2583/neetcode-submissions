class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, int> hashs;
        unordered_map<char, int> hasht;
        for (int i = 0; i < s.length(); i++) {
            hashs[s[i]]++;
            hasht[t[i]]++;
        }
        return hashs == hasht;
    }
};
