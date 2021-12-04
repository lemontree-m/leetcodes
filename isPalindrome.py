#9.回文数
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        '''
        if x < 0:
            return False
        elif str(x)== str(x)[::-1]:
            return True
        else:
            return False
        ————————
        if str(x)== str(x)[::-1]:
            return True
        else:
            return False
		'''
		return str(x)== str(x)[::-1]