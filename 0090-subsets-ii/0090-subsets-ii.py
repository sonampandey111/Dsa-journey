class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        op = []

        def solve(index):
            ans.append(op[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                op.append(nums[i])
                solve(i + 1)
                op.pop()

        solve(0)
        return ans
