class Solution:
    def isValid(self, s: str) -> bool:
        # i take a stack, put things on stack if open type
        # if closed type and matches peek, pop
        #else, invalid
        # also, at end if stack not empty, then invalid
        brackets = {"[" : "]", "{" : "}", "(" : ")"}
        clos_brac = set(brackets.values())

        stack = []
        for brac in s:
            if brac in brackets:
                stack.append(brac)
            elif brac in clos_brac:
                if stack and brac == brackets.get(stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
        