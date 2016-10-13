class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return []
        n0 = -1
        n2 = n-1
        n1 = 0
        while n1<=n2:
            if nums[n1] == 0:
                n0 += 1
                nums[n1], nums[n0] = nums[n0], nums[n1]
            elif nums[n1] == 2:
                while n0 < n1 and nums[n2] == 2: n2 -= 1
                nums[n1], nums[n2] = nums[n2], nums[n1]
                n2 -= 1
            n1 += 1

solver = Solution()
a = [0,2,1,0,1,2]
solver.sortColors(a)
print a
