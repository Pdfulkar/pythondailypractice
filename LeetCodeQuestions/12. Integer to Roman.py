class Solution(object):
    def intToRoman(self, num: object) -> object:
        """
        :type num: int
        :rtype: str
        """
        #         list1 = [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]
        #         res = ""
        #         for i in range(-len(list1), 0):
        #             n = num % list1[i][1]
        #             while n != 0:
        #                 if n == 0:
        #                     res += list1[i][0]
        #                 else:
        #                     if n == 4:
        #                         res = res + "IV"
        #                     if n == 9:
        #                         res = res + "IX"
        #                     if n == 40:
        #                         res = res + "XL"
        #                     if n == 90:
        #                         res = res + "XC"
        #                     if n == 400:
        #                         res = res + "CD"
        #                     if n == 900:
        #                         res = res + "CM"
        #             for j in range(i, 0):
        #                 n = n % list1[j][1]
        #         return res
        #
        #
        # c = Solution().intToRoman(122)
        #
        # print(c)
        list1 = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
                 ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
        res = ""
        for sym,num1 in reversed(list1):
            if num // num1 !=0:
                count = num//num1
                res += (count*sym)
                num = num % num1
        return res
