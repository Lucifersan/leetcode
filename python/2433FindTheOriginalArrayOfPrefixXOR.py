class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return
        rv = list()
        rv.append(pref[0])
        for i in range(1, len(pref)):
            rv.append(pref[i]^pref[i-1])
        return rv