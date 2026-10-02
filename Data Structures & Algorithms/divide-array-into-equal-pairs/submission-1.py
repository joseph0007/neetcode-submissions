class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ndict = {}
        for num in nums:
            nstr = str(num)
            if ndict.get(nstr):
                ndict[nstr] += 1
            else:
                ndict[nstr] = 1
        for num in ndict.values():
            if num % 2 != 0:
                return False
        return True