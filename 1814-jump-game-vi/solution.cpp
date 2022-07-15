#include <iostream>
#include <deque>

using namespace std;

class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        deque<int> queue;
        for (int i = 0; i < nums.size(); i++) {
            while (!queue.empty() && queue.front() < i - k) {
                queue.pop_front();
            }
            nums[i] += (!queue.empty() ? nums[queue.front()] : 0);
            while (!queue.empty() && nums[i] >= nums[queue.back()]) {
                queue.pop_back();
            }
            queue.push_back(i);
        }
        return nums.back();
    }
};
