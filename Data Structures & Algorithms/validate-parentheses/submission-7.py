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
        
        if not bracket_stack:
            return True
        else:
            return False


        