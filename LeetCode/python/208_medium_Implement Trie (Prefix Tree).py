'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

# 2018-10-5
# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = None 
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        nodes = self.root
        lens = len(word)
        i = 0
        while i < lens:
            # print(nodes)
            if word[i] in nodes:
                nodes = nodes[word[i]]
            else:
                return False 
            i += 1
        if '#' in nodes:
            return True
        return False 


        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # print("--------------------")
        nodes = self.root
        lens = len(prefix)
        i = 0
        while i < lens:
            # print(nodes)
            if prefix[i] in nodes:
                nodes = nodes[prefix[i]]
            elif '#' in nodes:
                return False 
            else:
                return False
            i += 1

        return True 
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = ["WordDictionary","addWore","addWord","search"]
prefix = ["appl", "wo", "ADD", "add"]
words = ["applee", "addWord", "addWo"]
for i in word:
    obj.insert(i)

r1 = []
r2 = []
for w in words:
    r1.append(obj.search(w))

for p in prefix:
    r2.append(obj.startsWith(p))
print(r1, r2)