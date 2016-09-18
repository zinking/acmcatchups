class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0: return ""
        def decode(cnt,st,eds):
            #print '###',cnt,st,eds
            r1 = ""
            while st < n:
                pst = st
                while st < n and not (s[st].isdigit()) and not s[st] == "]": st+=1
                ped = st
                r1 += s[pst:ped]
                if st < n and s[st] == "]":
                    eds[0] = st
                    return r1*cnt
                nst = st
                while st < n and (s[st].isdigit()): st+=1
                ned = st
                ncnt = 1
                if ned>nst:
                    #print '#ncnt:',nst,ned,n,s[nst:ned]
                    ncnt = int(s[nst:ned])
                if st < n and s[st] == "[":
                    subed = [0]
                    st+=1
                    substr = decode(ncnt,st,subed)
                    st = subed[0]+1
                    r1 += substr
                elif st < n and s[st] == "]":
                    eds[0] = st
                    return r1
                elif st < n:
                    r1 += s[st]
                    st+=1
            return r1
            
        red = [0]
        return decode(1,0,red)

solver = Solution()
print solver.decodeString("3[a]2[bc]")
print solver.decodeString("3[a]cc2[bc]")
print solver.decodeString("3[a]2[bc]ac")
print solver.decodeString("3[a2[c]]")
print solver.decodeString("2[abc]3[cd]ef")
print solver.decodeString("3[a]")
print solver.decodeString("")
print solver.decodeString("abc")
