

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        pathStack = []
        lvlLen = 0
        lvlNum = 0
        maxPath = 0
        isFile = False
        for s in input:
            if s == ".":
                isFile = True
            if s == "\n":
                if len(pathStack)<=lvlNum:
                    pathStack.append(0)
                if lvlNum == 0:
                    pathStack[lvlNum] = lvlLen 
                else:
                    pathStack[lvlNum] = pathStack[lvlNum-1] + lvlLen 
                if isFile: maxPath = max(maxPath, pathStack[lvlNum] + lvlNum)

                #reset to process next path
                lvlLen = 0
                lvlNum = 0
                isFile = False
            elif s == "\t":
                lvlNum += 1
            else:
                lvlLen += 1
        if lvlLen > 0:
            if len(pathStack)<=lvlNum:
                pathStack.append(0)
            if lvlNum == 0:
                pathStack[lvlNum] = lvlLen 
            else:
                pathStack[lvlNum] = pathStack[lvlNum-1] + lvlLen 
            if isFile: maxPath = max(maxPath, pathStack[lvlNum] + lvlNum)


        return maxPath





print ""
solver = Solution()
s1 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print solver.lengthLongestPath(s1)
s2 = ""
print solver.lengthLongestPath(s2)
s3 = "abc.txt"
print solver.lengthLongestPath(s3)
s31 = "abcdefg\n\t"
print solver.lengthLongestPath(s31)

s4 = "abc\n\tabcd\n\tab.def"
print solver.lengthLongestPath(s4)
