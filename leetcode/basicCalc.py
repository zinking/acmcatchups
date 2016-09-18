class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calc(op1, op2, op):
            if op == '+': return op1 + op2
            elif op == '-': return op1 - op2 
            elif op == '*': return op1 * op2
            elif op == '/': return op1 / op2
            return None
        dstack = []
        ostack = []
        opm = {'+':1,'-':1,'*':4,'/':4,'(':100,')':0}
        pos = opm.keys()
        s = filter(lambda x:x!=' ', s)
        n = len(s)
        st = 0 
        ed = st
        import pdb
        #pdb.set_trace()
        while ed < n :
            while ed < n and s[ed] not in pos: 
                ed += 1
            if ed>st:
                d1 = int(s[st:ed])
                dstack.append(d1)
            if ed >= n: continue
            op = s[ed]
            st = ed+1
            ed = st
            if len(ostack) == 0:
                ostack.append(op)
            else:
                lop = ostack[-1]
                if op == ')':
                    while lop != '(' :
                        op2 = dstack.pop()
                        op1 = dstack.pop()
                        r = calc(op1,op2,lop)
                        dstack.append(r)
                        ostack.pop()
                        lop = ostack[-1]
                    ostack.pop()
                elif op == '(':
                    ostack.append(op)
                elif opm[op] > opm[lop]:
                    #print ostack,dstack
                    ostack.append(op)
                else:
                    #print ostack,dstack
                    lop = ostack[-1]
                    while lop != '(' and opm[op] <= opm[lop]:
                        if len(ostack) > 0:
                            op2 = dstack.pop()
                            op1 = dstack.pop()
                            r = calc(op1,op2,lop)
                            dstack.append(r)
                            ostack.pop()
                            if len(ostack) == 0: break
                            lop = ostack[-1]
                    ostack.append(op)
        #print '#3:',ostack,dstack
        while len(ostack) > 0:
            lop = ostack.pop()
            op2 = dstack.pop()
            op1 = dstack.pop()
            r = calc(op1,op2,lop)
            dstack.append(r)

        return dstack[-1]
                

solver = Solution()
inputs = [
    "0",
    "(1+(4+5+2)-3)+(6+8)",
    " 2-1 + 2 ",
    "1 + 1",
    "3+2*2",
    " 3+5 / 2 ",
    " 3/2 ",
    "1+2-3*(4/5)+6-7*8/9+10-11",
    "1*2-3/4+5*6-7*(8+9)/10",
    "10-20*(30- 40)",
    " ( 3 ) "
]
inputss = [inputs[-2],inputs[-3]]
inputss = [inputs[-1]]
for input in inputs:
    print solver.calculate(input), 'exp:',eval(input)
