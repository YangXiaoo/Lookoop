"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

# 2020-9-24
# This python solution is quick and straightforward.

# The idea is to make a global counter and increment it whenever we find a new substring.

# The first step in the recursion function is getting a distinct set of remaining characters. Python makes this easy, just cast the input list as a set. Next iterate through the elements of the set, each time we hit a new element we want to increment the counter. This will make sure we increment when our current string length is less than the number of tiles. Next clone the original list, so we don't mess up the original for future iterations. Remove the first element of the current tile from the cloned list and pass that list to the recurse function.

# Short, simple, elegant Python code:

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.cnt = 0                                                      #make a counter at the class level
        self.recurse(tiles)                                               #call the rersion
        return self.cnt

    
    def recurse(self, tiles):
        tset = set(tiles)                                                 #get remaining distinct tiles
        for i in tset:                                                    #iterate through the distinct tiles
            self.cnt += 1                                                 #increment
            tiles2 = [j for j in tiles]                                   #clone the tileset
            tiles2.remove(i)                                              #remove the current tile
            self.recurse(tiles2)                                          #recurse

    def numTilePossibilities2(self, tiles):
        def helper(index, visited):
            nonlocal tiles, num
            if index == len(tiles):
                return

            i = 0 
            while i < len(tiles):
                if visited[i]:
                    i += 1
                    continue
                num += 1
                visited[i] = True 
                helper(index + 1, visited)
                visited[i] = False

                while i < len(tiles) - 1 and tiles[i] == tiles[i + 1]:
                    i += 1

                i += 1
            

        visited = [False for _ in tiles]
        num = 0
        helper(0, visited)

        return num

tiles = "AAB"
test = Solution()
ret = test.numTilePossibilities2(tiles)
print(ret)


# class Solution {
#     int num;
#     public int numTilePossibilities(String tiles) {
#         if (tiles.length() == 0) {
#             return 0;
#         }
        
#         num = 0;
#         boolean[] visited = new boolean[tiles.length()];
#         char[] chars = tiles.toCharArray();
        
#         Arrays.sort(chars);
        
#         DFS(visited, chars, 0);
        
#         return num;
#     }
    
#     private void DFS(boolean[] visited, char[] chars, int len) {
        
#         if (len == chars.length) {
#             return;
#         }
        
#         for (int i = 0; i < chars.length; i++) {
#             if (visited[i]) {
#                 continue;
#             }
            
#             num++;
#             visited[i] = true;
#             DFS(visited, chars, len + 1);
#             visited[i] = false;
            
#             while (i < chars.length - 1 && chars[i] == chars[i + 1]) {
#                 i++;
#             }
#         }
#     }
# }