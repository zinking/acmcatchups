__author__ = 'awang'


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def top(ps):
            if len(ps)>0:
                te = ps[-1]
                rr = 0
                while len(ps)>0 and te>=0:
                    rr+=te
                    ps.pop()
                    te = ps[-1] if len(ps)>0 else None
                return te,rr
            else:
                return None,0
        def push(ps,num):
            if len(ps)>0:
                rr=0
                te=ps[-1]
                while len(ps)>0 and te>=0:
                    rr+=te
                    ps.pop()
                    te=ps[-1] if len(ps)>0 else None
                ps.append(rr+num)
            else:
                ps.append(num)

        n=len(s)
        if n<2: return 0
        ps = [] #parenthese stack
        i = 0
        while i<n :
            te,rr = top(ps)
            if te == -1 and s[i] == ')':
                ps.pop()
                push(ps,rr+2)
            else:
                num = -1 if s[i] == '(' else -2
                ps.append(num)
            i+=1
        return max(ps)


if __name__ == '__main__':
    solution = Solution()
    print solution.longestValidParentheses("()()")