class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            ni = nums[i]
            while ni != i+1 and ni > 0:
                nit = ni-1
                nni = nums[nit]
                if ni == nni:
                    nums[nit] = -1
                    nums[i] = -2
                    break
                else:
                    nums[nit] = ni
                    nums[i] = nni
                    ni = nni
                    print nums
        print nums
        r = []
        for i in range(n):
            if nums[i] == -1: r.append(i+1)
        return r

s = Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])
