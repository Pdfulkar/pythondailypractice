class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_str= ""
        new_str = s.replace("AB","")
        final_str = new_str.replace("CD","")
        n = 0
        while n <(len(s)//2):
            new_str = final_str.replace("AB","")
            new_str = new_str.replace("CD","")
            final_str = new_str
            n +=1

        return len(final_str)


