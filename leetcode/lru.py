class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d={}
        self.c=capacity
        self.mints = 0
        self.cts = 0
        self.n = 0
        self.k2t = {}
        self.t2k = {}

    def get(self, key):
        """
        :rtype: int
        """
        if self.d.has_key(key):
            val = self.d[key]
            self.update_ts(key)
            return val
        else:
            return -1
    def update_ts(self,key,add=False):
        if not add:
            ts = self.k2t[key]
            del self.t2k[ts]
        self.cts+=1
        ts=self.cts
        self.k2t[key]=ts
        self.t2k[ts]=key
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.d.has_key(key):
            self.d[key]=value
            self.update_ts(key)
            return
        if self.n < self.c:
            self.d[key]=value
            self.n+=1
            self.update_ts(key,add=True)
        else:
            while( not self.t2k.has_key(self.mints) ):
                self.mints+=1
            mts = self.mints
            okey = self.t2k[mts]
            del self.d[okey]
            del self.k2t[okey]
            del self.t2k[mts]
            self.n-=1
            self.set(key,value)

if __name__ == '__main__':
    #2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]
    l = LRUCache(2)
    l.set(2,1)
    l.set(2,2)
    l.get(2)
    l.set(1,1)
    l.set(4,1)
    l.get(2)
if __name__ == '__main__1':
    l = LRUCache(10)
    for i in range(1,20):
        l.set(i,i)
    for i in range(1,20):
        print l.get(i)

