class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        sent = []
        allsent = []
        self.wordBreakUp(s,dict,sent,allsent)
        r = map(lambda wdlist:" ".join(wdlist),allsent)
        r.sort()
        return r

    def feasibleDict(self,s,dict):
        dictLetters = set();
        sentLetters = set();
        for ch in s: sentLetters.add(ch)
        for w in dict:
            for ch in w:
                dictLetters.add(ch)
        for ch in sentLetters:
            if ch not in dictLetters:
                return False
        return True

    def wordBreakUp(self,s,dict,sent,allsent):
        wdict = filter( lambda x:x in s, dict)
        if s == "":allsent.append(sent)
        if not self.feasibleDict(s,dict):
            return
        for w in wdict:
            wn = len(w)
            nsent = list(sent)
            i=0
            while s[i:i+wn]==w:
                nsent.append(w)
                i+=wn
            if i>0: self.wordBreakUp(s[i:],wdict,nsent,allsent)


if __name__ == '__main__':
    s=Solution()
    print s.wordBreak("a",["a"])
    print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    import pdb
    pdb.set_trace()
    print s.wordBreak("aaaaaaa",["aaaa","aaa"])

    print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

    print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabab",["a","aa","ba"])