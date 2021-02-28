# make a tracker list and pop the last element if there is a match

class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        for char in s:
            if char in ['(', '[', '{']:
                tracker.append(char)
            elif len(tracker) == 0:
                return False
            elif char == ')' and tracker[-1] != '(':
                return False
            elif char == ']' and tracker[-1] != '[':
                return False
            elif char == '}' and tracker[-1] != '{':
                return False
            else:
                tracker.pop()
        return len(tracker) == 0