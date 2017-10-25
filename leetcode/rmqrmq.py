import math
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        rmqn = int(math.sqrt(n))
        rmq = [0 for i in range(n/rmqn+1)]
        i = 0
        ii = 0
        while i < n:
            rmq[ii] += nums[i]
            if (i+1) % rmqn == 0: ii += 1
            i += 1
        self.rmq = rmq
        self.rmqn = rmqn
        self.nums = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        rmqn = self.rmqn
        ir = i/rmqn 
        jr = j/rmqn
        ssm = 0
        ssp = 0
        ss = 0
        for ii in range(ir*rmqn,i):
            ssm += self.nums[ii]
        for ii in range(ir,jr):
            ss += self.rmq[ii]
        for ii in range(jr*rmqn,j+1):
            ssp += self.nums[ii]

        print ir,jr,self.rmq,self.rmqn
        print ss,ssp,ssm
        return ss + ssp - ssm
        


# Your NumArray object will be instantiated and called as such:
nums = [1,2,3,4,5,6,7]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(1, 2)
