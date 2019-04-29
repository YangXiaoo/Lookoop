/*
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
*/

// 2019-4-29
// 771. Jewels and Stones [easy]
// https://leetcode.com/problems/jewels-and-stones/

import java.util.*;

public class JewelsandStones {
    public int numJewelsInStones(String J, String S) {
        int[] jewels = new int[58];
        for (int i = 0; i < J.length(); ++i)  {
        	jewels[J.charAt(i) - 'A']++;
        }

        int ret = 0;
        for (int s = 0; s < S.length(); ++s) {
        	ret += jewels[S.charAt(s) - 'A'];
        }

        return ret;
    }	
}
/* c++:
    int numJewelsInStones(string J, string S) {
        int jewels[58] = {0};	// 不初始化为0会有问题
        for (int i = 0; i < J.size(); ++i) {
            jewels[J[i] - 'A']++;
        }
        
        int ret = 0;
        for (int j = 0; j < S.size(); ++j) {
            ret += jewels[S[j] - 'A'];
        }
        
        return ret;
    }
*/