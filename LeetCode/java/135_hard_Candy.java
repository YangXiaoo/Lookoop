/**
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
*/

// 2018-7-23
// 135. Candy
class 135_hard_Candy {
    public int candy(int[] ratings) {
        if (ratings.length == 0) return 0;
        if (ratings.length == 1) return 1;

        int res[] = new int[ratings.length];
        res[0] = 1;
        int h = 0;

        for (int i = 1; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                h =  i;
                res[i] = res[i-1] + 1;
            }

            if (ratings[i] <= ratings[i - 1]) {
                if (ratings[i] == ratings[i - 1]) h = i;
                res[i] = 1;
                for (int j = i; j > h; j--) {
                    if (res[j] >= res[j - 1]) {
                        res[j - 1] += 1;
                    } // ~~~ end if
                } // ~~~ end for 
            } // ~~~ end if
        } // ~~~ end for

        int sum = 0;
        for (int n : res) {
            sum += n;
        }

        return sum;
    }
} 