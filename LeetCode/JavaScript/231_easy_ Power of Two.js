/**
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

**/

// 231. Power of Two - Easy
// 2019/10/21

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n == 0) {
        return false;
    }
    
    while (n >= 2) {
        n = n / 2;
    }
    return n === 1 ? true:false;
};

// test
console.log(true === isPowerOfTwo(3))	// false