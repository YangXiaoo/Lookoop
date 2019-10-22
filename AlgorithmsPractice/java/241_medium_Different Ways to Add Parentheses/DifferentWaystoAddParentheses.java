/*
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
*/

// 2019-5-31
// 241. Different Ways to Add Parentheses [medium]
// https://leetcode.com/problems/different-ways-to-add-parentheses

import java.util.*;

class DifferentWaystoAddParentheses {
    public List<Integer> diffWaysToCompute(String input) {
        // 分而治之
        List<Integer> ret = new ArrayList<>();
        for (int i = 0; i < input.length(); ++i) {
            if (input.charAt(i) == '+' || input.charAt(i) == '-' || input.charAt(i) == '*') {
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i + 1, input.length()));
                for (int j = 0; j < left.size(); ++j) {
                    for (int k = 0; k < right.size(); ++k) {
                        if (input.charAt(i) == '+') {
                            ret.add(left.get(j) + right.get(k));
                        } else if (input.charAt(i) == '-') {
                            ret.add(left.get(j) - right.get(k));
                        } else {
                            ret.add(left.get(j) * right.get(k));
                        }
                    }
                }
            }
        }

        if (ret.isEmpty()) {
            ret.add(Integer.valueOf(input));
        }

        return ret;
    }

    public void test(String testName, String input) {
        List<Integer> ret = diffWaysToCompute(input);
        System.out.println(testName + ", ret: " + ret.toString());
    }

    public static void main(String[] args) {
        String input1 = "2*3-4*5";
        DifferentWaystoAddParentheses test = new DifferentWaystoAddParentheses();
        test.test("test-1", input1);

    }
}