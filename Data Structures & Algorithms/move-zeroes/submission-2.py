class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_ptr = 0
        nz_ptr = 0
        l_num = len(nums)

        while True:
            while z_ptr < l_num and nums[z_ptr] != 0:
                z_ptr += 1
            
            while nz_ptr < l_num and (nums[nz_ptr] == 0 or nz_ptr < z_ptr):
                nz_ptr += 1

            if nz_ptr >= l_num or z_ptr >= l_num:
                break

            temp = nums[z_ptr]
            nums[z_ptr] = nums[nz_ptr]
            nums[nz_ptr] = temp






        