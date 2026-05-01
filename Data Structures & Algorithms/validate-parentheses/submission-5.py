class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = { "(" : ")", "{": "}", "[": "]"}

        stack = []
        for brac in s:
            if brac in bracket_map.keys():
                stack.append(brac)
            elif stack and bracket_map[stack[-1]] == brac:
                stack.pop()
            else:
                return False
        return len(stack)==0
        