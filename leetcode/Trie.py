class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.abc = [None for i in range(28)]
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        def insertTrieChar(trie,word,i,n):
            if i >= n: return
            chi = ord(word[i]) - ord('a')
            chTrie = trie.abc[chi]
            if chTrie is None:
                trie.abc[chi] = TrieNode()
                chTrie = trie.abc[chi]
            return insertTrieChar(chTrie,word,i+1,n)
        word += chr(ord('a') + 26)
        insertTrieChar(self.root, word, 0, len(word))

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def searchTrieChar(trie, word, i, n):
            if i == n: return True
            chi = ord(word[i]) - ord('a')
            chTrie = trie.abc[chi]
            if chTrie is None: return False
            return searchTrieChar(chTrie, word, i+1, n)
        word += chr(ord('a') + 26)
        return searchTrieChar(self.root, word, 0, len(word))
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def searchTrieChar(trie, word, i, n):
            if i == n: return True
            chi = ord(word[i]) - ord('a')
            #print '#',word[i], chi
            chTrie = trie.abc[chi]
            if chTrie is None: return False
            return searchTrieChar(chTrie, word, i+1, n)
        return searchTrieChar(self.root, prefix, 0, len(prefix))


trie = Trie()
trie.insert("somestring")
trie.insert("some")
print trie.search("key")
print trie.search("some")
print trie.search("somet")
print trie.search("somethingsss")
print trie.startsWith("some")
print trie.startsWith("somez")
