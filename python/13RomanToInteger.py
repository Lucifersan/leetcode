#easiest thing ever
#taught me to remember that dictionaries exist
class Solution:
    def romanToInt(self, s: str) -> int:
        intList = []
        thisdict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        diffSet = {4, 9, 40, 90, 400, 900}
        rv = 0
        for i in s:
            intList.append(thisdict[i])
        for i, n in enumerate(intList):
            if i == 0:
                rv += n
            else:
                rv += n
                if n > intList[i-1] and abs(n-intList[i-1]) in diffSet:
                    rv -= 2*intList[i-1]
        return rv
            
        