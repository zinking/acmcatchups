from math import sqrt 
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        an = int(sqrt(n))
        na = n / an + 1 if an > 0 else 0
        self.nums = nums
        self.an = an
        self.na = na
        self.summary = [0 for i in range(na)]

        i = 0
        nk = 0
        while i < n:
            sn = 0
            ni = 0
            while ni < an and i<n:
                sn += nums[i]
                ni += 1
                i += 1
            self.summary[nk] = sn
            nk += 1

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.nums[i]
        nk = i / self.an if self.an > 0 else 0
        self.summary[nk] += delta
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sk = i / self.an if self.an > 0 else 0
        ek = j / self.an if self.an > 0 else 0
        total = 0
        for si in range(sk,ek):
            total += self.summary[si]
        toMinus = 0
        for si in range(sk*self.an, i):
            toMinus += nums[si]
        toPlus = 0
        for si in range(ek*self.an, j+1):
            toPlus += nums[si]
        #print '#',total, toMinus, toPlus
        return total - toMinus + toPlus


# Your NumArray object will be instantiated and called as such:
nums = range(1,10)
numArray = NumArray(nums)
print '#',numArray.nums
print '#',numArray.summary

print numArray.sumRange(0, 2)
numArray.update(1, 0)
print '#',numArray.nums
print '#',numArray.summary
print numArray.sumRange(0, 2)
print numArray.sumRange(0, 5)
print numArray.sumRange(0, 8)
print numArray.sumRange(0, 7)

