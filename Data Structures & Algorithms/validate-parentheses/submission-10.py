class Solution:
    def isValid(self, s: str) -> bool:
        bracket_open_close_map = {'(': ')', '{': '}', '[' : ']'}
        bracket_stack = []

        for char in s:
            if char in bracket_open_close_map:
                #char is a opening bracket
                bracket_stack.append(char)
            elif char in bracket_open_close_map.values():
                #char is a closing bracket'
                if bracket_stack:
                    opening_bracket = bracket_stack.pop()
                    if not bracket_open_close_map[opening_bracket] == char:
                        return False
                else:
                    return False
            else:
                return False
        
        return len(bracket_stack)==0


# Yes, exactly! A good follow up is 👌

# If the string is a full mathematical expression like "3 + (2 - [5 * {4 / (2 + 1)}])", and your goal is only to validate the brackets, then you:
# 	•	Still use a stack to track brackets,
# 	•	But ignore all non-bracket characters.
