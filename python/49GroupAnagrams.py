#disgustingly written and disgustingly slow
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for s in strs:
            temp={}
            for c in s:
                if c not in temp:
                    temp[c]=0
                temp[c]+=1
            listed = [0 for i in range(26)]
            for i in temp:
                listed[ord(i)-ord("a")] = temp[i]
            if tuple(listed) not in count:
                count[tuple(listed)]=list()
            count[tuple(listed)].append(s)

        rv = list()
        for i in count:
            rv.append(count[i])
        return rv

            