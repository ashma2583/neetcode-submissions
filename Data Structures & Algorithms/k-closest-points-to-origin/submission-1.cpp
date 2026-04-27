class DistanceGreater {
public: 
    bool operator()(const vector<int> &p1, const vector<int> &p2) const {
        return (p1[0] * p1[0] + p1[1] * p1[1]) > (p2[0] * p2[0] + p2[1] * p2[1]);
    }
};


class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, DistanceGreater> minHeap(points.begin(), points.end());
        vector<vector<int>> output;

        for (int i = 0; i < k; i++) {
            output.push_back(minHeap.top());
            minHeap.pop();
        }

        // vector<int> top = minHeap.top();
        // minHeap.pop();
        // int shortest = (top[0] * top[0] + top[1] * top[1]);
        // vector<int> next = minHeap.top();
        // while ((next[0] * next[0] + next[1] * next[1]) == shortest) {
        //     output.push_back(next);
        //     minHeap.pop();
        //     next = minHeap.top();
        // }
        return output;
    }
};
