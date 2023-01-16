class Solution:

    def canJump(self, nums: list[int]) -> bool:
        max_jump = 0
        idx = 0

        while idx <= max_jump:
            max_jump = max(max_jump, idx + nums[idx])

            if max_jump >= len(nums) - 1: return True

            idx += 1

        return False


    # Outras tentativas
    ############################################################################
    # def check_max_jump(self, idx: int, next_max_idx: int, size: int, nums: list[int]) -> bool:
    #     for current_sum in range(1, next_max_idx + 1, 1):
    #         if idx + current_sum >= size - 1:
    #             return True

    #         if idx + current_sum > size - 1 or idx + current_sum == idx: 
    #             continue
            
    #         if self.check_max_jump(idx + current_sum, nums[idx + current_sum], size, nums):
    #             return True
        
    #     return False


    # def canJump(self, nums: list[int]) -> bool:
        # idx = 0
        # next_max_idx = nums[idx]
        # size = len(nums)

        # if size == 1:
        #     return True
        
        # return True if self.check_max_jump(idx, next_max_idx, size, nums) else False
        ########################################################################
        # while True:
        #     next_max_idx += nums[idx]

        #     check = self.check_max_jump(idx, next_max_idx, size)

        #     if check: return True
        #     if not check and next_max_idx > size -1 or next_max_idx == idx: return False
            
        #     idx = next_max_idx
        ########################################################################
        # max_jump = 0
        # idx = 0

        # while idx <= max_jump:
        #     max_jump = max(max_jump, idx + nums[idx])

        #     if max_jump >= len(nums) - 1: return True

        #     idx += 1

        # return False
        ########################################################################
        # for current in list(range(0, idx - 2, 1))[::-1]:
        #     if nums[current] + current >= idx - 1:
        #         idx = current
        
        # return True if idx - 1 == 0 else False
            
            