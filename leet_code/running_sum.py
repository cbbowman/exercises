from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [nums[0]]

        for n in nums[1:]:
            running_sum.append(n + running_sum[-1])

        return running_sum


s = Solution()
print(s.runningSum([1, 2, 3, 4, 5, 6]))
