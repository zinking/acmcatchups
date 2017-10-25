class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = 0
        n = len(nums)
        if n == 0: return False
        big = 0
        for k in nums:
            big = max(big,k)
            total += k
        if total%4 != 0 : return False

        avg = total/4
        if big > avg: return False
        def change(nums, current, total):
            if len(nums) == 0 and current == 0 and total == 4:
                return True
            if current > avg:
                return False
            if current == avg:
                return change(nums,0,total+1)
            r = False
            for k in nums:
                nnums = list(nums)
                nnums.remove(k)
                tr = change(nnums, current+k, total)
                if tr:
                    r = True
                    break
            return r
        return change(nums,0,0)


solver = Solution()
print solver.makesquare([211559,9514615,7412176,5656677,3816020,452925,7979371,5025276,8882605,944541,9889007,2344356,7252152,749758,2311818])
