class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int> strengths;
        for (int i = 0; i < mat.size(); i++){
            int temp = 0;
            for (int j = 0; j < mat[i].size(); j++)
                if (mat[i][j] == 1) temp++;
            strengths.push_back(temp);
        }

        vector<int> ranks;
        for (int i = 0; i < k; i++){
            int minIndex = min_element(strengths.begin(), strengths.end()) - strengths.begin();
            strengths[minIndex]=10000000;
            ranks.push_back(minIndex);
        }

        return ranks;
    }
};
