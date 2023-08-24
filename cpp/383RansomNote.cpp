class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int noteCounts[26];
        int magCounts[26];
        for (int i = 0; i < 26; i++) noteCounts[i] = 0;
        for (int i = 0; i < 26; i++) magCounts[i] = 0;

        for (int i = 0; i < ransomNote.size(); i++) noteCounts[ransomNote[i]-'a']++;
        for (int i = 0; i < magazine.size(); i++) magCounts[magazine[i]-'a']++;

        for (int i = 0; i < 26; i++) if(magCounts[i] < noteCounts[i]) return false;
        return true;
    }
};
