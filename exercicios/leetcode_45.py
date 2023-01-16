# 45. Jump Game II

class Solution:

    def jump(self, nums: list[int]) -> int:
        current = -1
        jumps = 0
        size = len(nums)
        idx = 0
        next_jump = 0

        while size - 1 > next_jump:

            if idx > current:
                jumps += 1
                current = next_jump

            next_jump = max(next_jump, nums[idx] + idx)
            idx += 1
        
        return jumps
