#stupid and a bit slow but works
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        rv = list()
        curr = [0 for i in range(26)]
        removed = 1
        for word in words:
            temp = [0 for i in range(26)]
            for c in word:
                temp[ord(c)-ord("a")]+=1
            if temp != curr:
                removed += 1
                curr = [a for a in temp]
                rv.append(word)
        return rv
