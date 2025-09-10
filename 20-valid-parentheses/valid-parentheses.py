class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {')':'(', ']':'[', '}':'{'}
        stk = []
        for i in s:
            if i in p.values():
                stk.append(i)
            elif i in p.keys():
                if not stk or p[i] != stk[-1]:
                    return False
                else :
                    stk.pop()
            else:
                return False
        if len(stk) == 0:
            return True
        return False