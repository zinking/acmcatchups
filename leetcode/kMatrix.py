import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        
        l = matrix[0][0]
        h = matrix[n-1][n-1]
        ck = 0 
	e = 0
        while l <= h:
            m = l + (h - l)/2
            l1 = bisect.bisect_left(matrix[0], m)
            if l1 == n: l1 = n - 1
            ck = l1 + 1
            j = 1
            while j < n:
                if m >= matrix[j][l1]:
                    ck += (l1 + 1)
                    j += 1
                else:
                    break
	    j -= 1
	    if j + 1 < n:
		l1 = bisect.bisect_left(matrix[j+1], m)
		if l1 == n: l1 = n - 1
		ck += (l1 + 1)
		j += 1
	    print 'l:%d h:%d m:%d ck:%d j:%d l1:%d'%(l,h,m,ck,j,l1)
	    e = matrix[j][l1]
            if ck == k : return e
            elif ck > k : h = m - 1
            elif ck < k : l = m + 1
        return e


s = Solution()
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],7)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],6)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],5)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],4)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],3)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],2)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],1)
print s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],9)

        
          
