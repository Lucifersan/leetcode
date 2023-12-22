#Simple and easy
#not optimal or best codewriting, does the trick
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i]= s_dict[i]+1
            else:
                s_dict[i]=1
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1
        for i in s_dict:
            if i in t_dict and s_dict[i]==t_dict[i]:
                pass
            else:
                return False
        for i in t_dict:
            if i in s_dict and t_dict[i]==s_dict[i]:
                pass
            else:
                return False
        return True
        
#potentially more optimal space-wise: constant size 26 array