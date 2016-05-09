__author__ = 'awang'

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        n=len(s)
        if n==0:return ""
        for i in range(n):
            c = s[i]
            if d.has_key(c):
                d[c].append(i)
            else:
                d[c]=[i]

        self.found = False
        self.items = sorted(d.items())
        self.itemsn = len(d)
        def dfs(row, r, tpos ):
            if self.found:return
            if len(r)==self.itemsn:
                self.found = True
                self.r = r
                return
            pos = self.items[row][1]
            for p in pos:
                if p>tpos:
                    oldr = r
                    r+=s[p]
                    dfs(row+1,r,p)
                    r=oldr
        dfs(0,"",-1)
        return self.r


s = Solution()

print s.removeDuplicateLetters("cbacdcbc")
print s.removeDuplicateLetters("bcabc")

print s.removeDuplicateLetters("")
print s.removeDuplicateLetters("abacb")
