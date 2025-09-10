#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;

        // Step 1: Sort nums
        sort(nums.begin(), nums.end()); 
        // Sorting ensures duplicates are next to each other,
        // making it easier to handle them.

        set<vector<int>> st;  
        // 'set' will automatically remove duplicate subsets

        int subsets = 1 << n; // total subsets = 2^n

        // Step 2: Loop through all subset bitmasks
        for (int num = 0; num < subsets; num++) {
            vector<int> curr; 

            // Step 3: Build subset based on bits
            for (int i = 0; i < n; i++) {
                if (num & (1 << i)) { 
                    // If ith bit is set → include nums[i]
                    curr.push_back(nums[i]);
                    cout << nums[i] << " ";
                }
            }
            cout << "\n";
            // Step 4: Insert subset into set (duplicates auto removed)
            st.insert(curr);
        }

        // Step 5: Convert set to vector
        for (auto it : st) {
            ans.push_back(it);
        }

        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = sol.subsetsWithDup(nums);

    cout << "Unique subsets are:\n";
    for (const auto& subset : result) {
        cout << "[ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "]\n";
    }

    return 0;
}