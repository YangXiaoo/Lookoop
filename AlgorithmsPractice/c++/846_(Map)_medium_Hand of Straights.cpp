/* 
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
===================================================================
*/
// 2018-8-30
// 846. Hand of Straights
// https://leetcode.com/problems/hand-of-straights/description/

// https://leetcode.com/problems/hand-of-straights/discuss/135598/C++JavaPython-O(MlogM)-Complexity
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        map<int, int> counter;
        for (auto i : hand) counter[i] += 1;

        for (auto c : counter)
        {
        	for (int j = w - 1; j >= 0; j--)
        	{
        		// 每连续个w的次数减去第一个数出现的次数，如果不小于0则可以组合。
        		if (counter[c.first - j] -= counter[c.first] < 0) return false;
        	}
        }

        return true;
    }
};