""" 
DIFFICULTY:  Easy
PROBLEM:     0412. Fizz Buzz
             https://leetcode.com/problems/fizz-buzz
PATTERN:     Arrays
"""

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        r = [None] * n
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                r[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                r[i-1] = "Fizz"
            elif i % 5 == 0:
                r[i-1] = "Buzz"
            else:
                r[i-1] = str(i)
        return r 