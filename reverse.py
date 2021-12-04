#7.整数反转
class Solution:
    def reverse(self, x: int) -> int:
        rl = []
        sign = ""
        for i in str(x):
            if i == "-":
                sign = i
            else:
                rl.append(i)
        rl.reverse()
        y = sign + "".join(rl)
        y = int(y)
        if y > 2**31-1 or y < -2**31:
            return 0
        else:
            return int(y)