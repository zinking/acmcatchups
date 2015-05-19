
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate1(self, nums, k):
        n = len(nums)
        k = (n-k)%n
        if k==0: return
        nums2 = nums+nums
        nums0 = nums2[k:k+n]
        for i in range(n): nums[i] = nums0[i]
        
    def rotate2(self, nums, k):
	def swap(nums, i, j ):
	    tmp = nums[i]
	    nums[i]=nums[j]
	    nums[j]=tmp

	def bubble( nums, i, n ):
	    for k in range(i,n-1):
		swap(nums,k,k+1)
	    
        n = len(nums)
	k = k%n
	if k <= n/2:
	    nb = n-k-k
	    if k==0: return
	    for i in range(nb):
		bubble(nums,k,n)
		#print nums
	    #print n,nb,k,nums
	    for i in range(k):swap(nums,i,k+i)
	else:
	    for i in range(n-k):
		bubble(nums,0,n)

    def rotate3(self,nums,k):
	n = len(nums)
	k = k%n
	def reverse(nums,m,n):
	    i=m
	    j=n-1
	    while i<j:
		nums[i],nums[j]=nums[j],nums[i]
		i+=1
		j-=1
	reverse(nums,0,n-k)
	reverse(nums,n-k,n)
	reverse(nums,0,n)

    def rotate(self,nums,k):
	n = len(nums)
	k=k%n
	while(k>0):
	    a = nums.pop()
	    nums.insert(0,a)
	    k-=1


s=Solution()
l1 = range(8)
s.rotate(l1,3)
print l1

l2 = [1]
s.rotate(l2,2)
print l2

l3 = [0,1,2]
s.rotate(l3,2)
print l3 
