"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""

import collections
def solution(inputString):
    c = collections.Counter(x[0] for x in inputString if x)
    count = 0
    for i in c.values():
        if i % 2 != 0:
            count += 1
    return False if count > 1 else True

inputString = "aabb"
print(solution(inputString))
inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
print(solution(inputString))
