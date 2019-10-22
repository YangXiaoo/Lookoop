/* 
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?

===================================================================
*/
// 2018-8-29
// 470. Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/description/
// http://www.cnblogs.com/xbinworld/p/4266146.html
// https://leetcode.com/problems/implement-rand10-using-rand7/discuss/150301/Three-line-Java-solution-the-idea-can-be-generalized-to-%22Implement-RandM()-Using-RandN()%22

// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7
class Solution {
public:
    int rand10() {
        int num;
        while (true)
        {
            // 得到1~49范围的数且每个值得概率都为1/49. 
            // we have P(A) = 7 * (rand7() - 1)= 1/7, P(B) = rand7() - 1 = 1/7. So P(AB) = P(A)P(B) = 1/49
            num = 7 * (rand7() - 1) + rand7() - 1;
            if (num < 40)
                // 当num < 40时，生成的1 - 9才能概率相同。例如当num = 42时，假设最后生成1则有有1,11,21,31,41五种可能，但若最后生成4则 可能取值为4,14,24,34四种可能，可见概率不一致。所以num必须取十的倍数
                return num % 10 + 1;
        }
    }
};