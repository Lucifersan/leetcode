class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector<int> wealth;
        for (int i = 0; i < accounts.size(); i++){
            int temp = 0;
            for (int j = 0; j < accounts[i].size(); j++) temp += accounts[i][j];
            wealth.push_back(temp);
        }

        return *max_element(wealth.begin(), wealth.end());
    }
};
