from collections import Counter
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sn = len(s)
        tn = len(t)
        cs = Counter(s)
        ct = Counter(t)
        if sn == 0 : return True
        def isCompatible(ct, cs):
            for ch,cnt in cs.items():
                if not ct.has_key(ch): return False
                if ct[ch] < cnt: return False
            return True
            
        if not isCompatible(ct,cs): return False
        
        pcs = Counter()
        pct = Counter()
        si = 0 
        ti = 0
        for si in range(sn):
            sch = s[si]
            pcs[sch] += 1
            while t[ti] != sch :
                tch = t[ti]
                pct[tch] += 1
                ti+=1
                
            if not isCompatible(ct-pct, cs-pcs): 
                return False
                
        return True
            
            

solver = Solution()
print solver.isSubsequence("a","ab")
print solver.isSubsequence("","a")
print solver.isSubsequence("axc","ahbgdc")
print solver.isSubsequence("abc","ahbgdc")
print solver.isSubsequence("abc","abc")
print solver.isSubsequence("abc","acb")
