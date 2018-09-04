'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''

# 2018-9-4
# 211. Add and Search Word - Data structure design
# Trie (前缀树)
# LeetCode 出现了一点问题！！！
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
        # {'b': {'a': {'d': {None: None}}}, 'd': {'a': {'d': {None: None}}}, 'm': {'a': {'d': {None: None}}}}

    # def search(self, word):
    #     nodes = [self.root]
    #     for char in word:
    #         nodes = [kid for node in nodes for kid in
    #                  ([node[char]] if char in node else
    #                   filter(None, node.values()) if char == '.' else [])]
    #     print(nodes)
    #     return any(None in node for node in nodes)
        
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