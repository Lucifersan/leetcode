class Solution:
    def myAtoi(self, s: str) -> int:
        rv = 0
        pos = True
        started = False
        firstsign = True
        for i in s:
            if i == " " and not started: started = False
            else: started = True
            if started:
                if i == "-" and firstsign: pos, firstsign = False, False
                elif i == "+" and firstsign: pos, firstsign = True, False
                elif i.isdigit(): rv, firstsign = 10*rv + int(i), False
                else: break
        rv = rv if pos else rv * -1
        rv = 2**31-1 if rv > 2**31-1 else rv
        rv = -2**31 if rv < -2**31 else rv
        return rv