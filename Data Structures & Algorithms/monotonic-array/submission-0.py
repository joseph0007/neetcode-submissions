class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        lnum = len(nums)

        inc = True
        i = 0
        j = i + 1
        while j < lnum:
            if nums[i] <= nums[j]:
                i += 1
                j += 1
            else:
                inc = False
                break

        dec = True
        i = 0
        j = i + 1
        while j < lnum:
            if nums[i] >= nums[j]:
                i += 1
                j += 1
            else:
                dec = False
                break
        
        return inc or dec