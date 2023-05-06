class Solution {
public:
    int romanToInt(string s) {
        int answer = 0;
        int n = s.length();
        vector<int> number;
        unordered_map<char, int> numKey;
        numKey['I'] = 1;
        numKey['V'] = 5;
        numKey['X'] = 10;
        numKey['L'] = 50;
        numKey['C'] = 100;
        numKey['D'] = 500;
        numKey['M'] = 1000;

        bool positive = true;
        int prevDigit = numKey[n-1];
        for (int i = n - 1; i >= 0; i-- ){
            int temp = numKey[s[i]];
            if (temp < prevDigit) positive = false;
            else positive = true;
            
            if(positive) answer += temp;
            else answer -= temp;

            prevDigit = temp;
        }

        return answer;
    }
};
