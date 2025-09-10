class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        original = x
        res = 0
        while x != 0:
            r = x % 10
            res = res * 10 + r
            x = x//10
        return original == res