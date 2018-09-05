# Trie 前缀树
# 2018-9-4
# https://segmentfault.com/a/1190000008877595

# 字典树
# 消耗空间来换得时间
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
    
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = None
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = self.root
        return self.search_dfs(word, nodes)
        
        
    def search_dfs(self, word, curr):
        # print("---------------", curr, word)
        word = "".join(word)
        if len(word)==0:
            return '#' in curr
        c = word[0]
        if c == '.':
            for char in curr:
                # print(char)
                return self.search_dfs(word[1:], curr[char])
        # now c is a-z
        if c in curr:
            return self.search_dfs(word[1:], curr[c])
        return False






# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

word = ["WordDictionary","addWore","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
for i in word:
    obj.addWord(i)
print(obj.root)
search = [['.'],["addWord"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
for i in search:
    param_2 = obj.search(i)
    print(param_2)