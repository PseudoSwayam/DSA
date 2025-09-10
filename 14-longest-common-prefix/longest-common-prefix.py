class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pr = strs[0]
        for i in strs[1:]:
            while not i.startswith(pr):
                pr = pr[:-1]
                if not pr:
                    return ""
        return pr
        