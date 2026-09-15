class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_min = 0
        curr_min = 0
        for idx,num in enumerate(nums):
            if idx == 0:
                curr_min += 1
            elif num < nums[idx-1]:
                curr_min += 1
            else:
                curr_min = 1
            max_min = max(max_min,curr_min)
        curr_max = 0
        max_max = 0
        for idx,num in enumerate(nums):
            if idx == 0:
                curr_max += 1
            elif num > nums[idx-1]:
                curr_max += 1
            else:
                curr_max = 1
            max_max = max(max_max,curr_max)
        return max(max_min,max_max)

        