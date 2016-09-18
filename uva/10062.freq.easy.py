import sys
from collections import Counter


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    n = len(lines)
    for i in range(n):
        line = lines[i][:-1]
        c = Counter(line)
        sc = sorted(c.items(), key=lambda x:(x[1],x[0]))
        for ch,n in sc: print ord(ch),n
        #for ch,n in sc: print (ch),n
        if i<n-1: print ""
