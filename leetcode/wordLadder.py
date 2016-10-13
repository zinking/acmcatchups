class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def d1(src, target):
            n = len(src)
            c = 0 
            for i in range(n):
                if src[i] != target[i]: c+= 1
            return c == 1
        wordList = list(wordList)
        md = [0x7fffffff]
        nn = len(wordList)
        v = [0 for i in range(nn)]

        def bfs(current, d):
            #print '#', current, d
            if d1(current, endWord):
                md[0] = min(d+1,md[0])
                return 
            cands = []
            for kk in range(nn):
                wd = wordList[kk]
                if d1(current,wd) and v[kk] == 0:
                    cands.append(wd)
                    v[kk] = 1
            for wd in cands:
                bfs(wd, d+1)
                v[kk] = 0  
        bfs(beginWord,1)
        return md[0] if md[0] < 0x7fffffff else 0

solver = Solution()
wordList = ["hot","dot","dog","lot","log"]
w1 = set(wordList)

print solver.ladderLength("hit","cog",w1)
