class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return None
        
        def radixSort(nums):
            print "Sort"*15
            buckets = [ [] for i in range(10)]
            allZero = False
            i = 1
            r = nums
            while not allZero:
                allZero = True
                for n in r:
                    di = (n/(10**(i-1)))%(10)
                    if di != 0: allZero = False
                    buckets[di].append(n)

                print i, buckets
                r = []
                for i1 in range(0,10):
                    r.extend(buckets[i1])
                    buckets[i1] = []
                print '#:',r
                i+=1
            return r
        snums = radixSort(nums)
        print snums
        return snums[k-1]
                

solver = Solution()
print ""
print solver.findKthLargest([1],1)
print solver.findKthLargest([-1,-1],2)
print solver.findKthLargest([10,128398,32,12321],1)
