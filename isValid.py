#20.有效的括号
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ["()","[]","{}"]
        lbracket = ["(","[","{"]
        rbracket = [")","]","}"]
        nl = []
        for ele in s:
            if ele in lbracket:
                nl.append(ele)
            else:
                if nl:
                    if (nl[-1] + ele) in brackets:
                        nl.pop()
                    else:
                        return False
                else:
                    return False       
        if nl:
            return False
        else:
            return True