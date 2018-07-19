/**

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
*/

// 2018-7-19
// 125. Valid Palindrome
class bcf_easy_Valid_Palindrome {
    public boolean isPalindrome(String s) {

        int l = 0, r = s.length() - 1;

        if (r < 0) return true;

        while (l < r) {
          char h = s.charAt(l), e = s.charAt(r);

          if (!Character.isLetterOrDigit(h)) l++;
          if (!Character.isLetterOrDigit(e)) r--;

          if (Character.isLetterOrDigit(h) && Character.isLetterOrDigit(e)) {
            if (Character.toLowerCase(h) != Character.toLowerCase(e)) return false;
            l++;
            r--;
          }

        }

        return true;
    }
}