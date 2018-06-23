"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
".1" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""
# 2018-6-23
# Valid Number
# Funny Job
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
        	float(s)
        	return True
        except:
        	return False

# test
s = ".1"
test = Solution()
res = test.isNumber(s)
print(res)
"""
I was asked in the interview of linkedIn, writing it directly can be extremely complicated, for there are many special cases we have to deal with, and the code I wrote was messy. Then I failed to pass the interview.

Here's a clear solution. With DFA we can easily get our idea into shape and then debug, and the source code is clear and simple.
"""
# Link: https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
# DFA(Deterministic Finite Automation)
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input) 
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input    
        if currentState not in [3,5,8,9]:
            return Fals

        
"""
title: The worst problem i have ever met in this oj
content: The description do not give a clear explantion of the definition of a valid Number, we just use more and more trick to get the right solution. It's too bad, it's waste of my time
f1:
sherry4869 0  2 days agoReport
can not agree more Can anyone adjust the test case?
f2:
csyfuzhou 0  April 14, 2018 4:56 PMReport
Exactly !!!!

How could "48." is a valid number !!!
f3:
annibalVox 4  April 8, 2018 4:22 PMReport
"You should gather all requirements." Great, post your cell phone number.
f4:
We should use python to f*ck this problem.
f5:

ArrivaL 1  January 15, 2018 4:28 PMReport
I agree with you.Nobody knows how many "if else" I've used but god！I submitted at least 10 times.
f:
cdai 914  January 29, 2017 9:51 AMReport
Agree, it made me feel frustrated and submitted again and again...
"""