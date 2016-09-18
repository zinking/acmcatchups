class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = len(data)
        i = 0 
        while i < n:
            u = data[i]
            if u >> 4 == 15 and i+3 < n:
                u1 = data[i+1]
                u2 = data[i+2]
                u3 = data[i+3]
                if u1 >> 6 == 2 and u2 >> 6 == 2 and u3 >> 6 == 2:
                    i+=4
                    continue 
            elif u >> 5 == 7 and i+2 < n:
                u1 = data[i+1]
                u2 = data[i+2]
                if u1 >> 6 == 2 and u2 >> 6 == 2:
                    i+=3
                    continue 
            elif u >> 6 == 3 and i+1 < n:
                u1 = data[i+1]
                if u1 >> 6 == 2:
                    i+=2
                    continue
            elif u >> 7 == 0:
                i+=1
                continue
            return False
        return True


solver = Solution()
print solver.validUtf8([197,130,1])
print solver.validUtf8([235, 140, 4])
