class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0: return ""
        if numerator == 0: return "0"
        sign = ""
        if numerator ^ denominator < 0: sign = "-"
        numerator = -numerator if numerator < 0 else numerator
        denominator = -denominator if denominator < 0 else denominator
        d = numerator//denominator
        m = numerator%denominator
        rr = []
        isCycle = False 
        cst = 0
        ced = 0
        lastPosMap = {}
        pos = 0
        import pdb
        while m != 0 and not isCycle:
            rm = m*10
            dd = rm//denominator
            m = rm%denominator
            rr.append(dd)
            if lastPosMap.has_key(rm):
                lastPos = lastPosMap[rm]
                olastPos = lastPos
                cycleLen = 0
                if rr[pos] == rr[lastPos]:
                    cycleLen = pos - lastPos
                oLen = cycleLen

                if len(rr) >= 2*cycleLen:
                    currPos = pos
                    isCycle = True

                    while (cycleLen > 0):
                        if (rr[lastPos] != rr[currPos]):
                            isCycle = False
                            break
                        lastPos -= 1
                        currPos -= 1
                        cycleLen -= 1
                    if isCycle:
                        #pdb.set_trace()
                        cst = olastPos - oLen + 1
                        ced = olastPos + 1
            lastPosMap[rm] = pos
            pos += 1

        rstr = ""
        if len(rr) > 0:
            rstr += "."
            if isCycle:
                ri = 0
                while ri < cst:
                    rstr += str(rr[ri])
                    ri += 1
                rstr += "("
                while ri < ced:
                    rstr += str(rr[ri])
                    ri += 1
                rstr += ")"
            else:
                ri = 0
                while ri < len(rr): 
                    rstr += str(rr[ri])
                    ri+=1

        return sign+str(d)+rstr

solver = Solution()

print solver.fractionToDecimal(1,4)
print solver.fractionToDecimal(1,3)
print solver.fractionToDecimal(1,7)
print solver.fractionToDecimal(1,70)
print solver.fractionToDecimal(1,99999)
#print solver.fractionToDecimal(1,19860611)
print solver.fractionToDecimal(-1,4)
print solver.fractionToDecimal(-1234,4)
