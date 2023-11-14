class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nset = set()
        res = []
        for i in nums:
            if i in nset:
                res.append(i)
            nset.add(i)
        return  res