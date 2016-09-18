class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0: return 0
        
        l = 0 
        h = n-1
        hindex = 0
        while l<=h:
            print '#',l,h
            m = l + (h-l)/2
            tm = min(citations[m],n-m)
            hindex = max(hindex,tm)
            if citations[m] >= m:
                h = m-1
            else:
                l = m+1
        return hindex


solver = Solution()
print solver.hIndex([0,0,0,0])
print solver.hIndex([4,4,4,4])
