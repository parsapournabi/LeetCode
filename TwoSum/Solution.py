from typing import *


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i, num in enumerate(nums):
            if i == len(nums) - 1 or i in ans:
                continue
            if num + nums[i + 1] == target:
               ans.append(i)
               ans.append(i + 1)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([3,2,4], 6))