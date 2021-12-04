#13.罗马数字转整数
class Solution:
    def romanToInt(self, s: str) -> int:
        romedict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        romedict2 = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        romenum = 0
        for x in romedict2:
            if x in s:
                romenum = romenum + romedict2[x]
                s = s.replace(x,"")
        for i in s:
            romenum = romenum + romedict[i]
        return romenum