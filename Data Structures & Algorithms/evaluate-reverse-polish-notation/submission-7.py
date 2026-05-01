class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_set = set(["+", "-", "*", "/"])

        #result stack
        result = []
        #[5]
        #traverse the list of tokens
        for t in tokens:
            print(result)
            #if not an operator
            if not t in operator_set:
                #assume it to be and integer and push it to stack
                result.append(t)
            else:
                #valid cases
                operand1 = int(result.pop())
                operand2 = int(result.pop())
                if t=="+":
                    result.append(operand2 + operand1)
                elif t=="-":
                    result.append(operand2 - operand1)
                elif t=="*":
                    result.append(operand2 * operand1)
                elif t=="/":
                    # result.append(round(operand2/operand1,0)) #but note round give results in float which might cause issues
                    #so btr
                    result.append(int(operand2/operand1))
                    #or import math and math.trunc(operand2/operand1)
                else:
                    return -1000
        
        return int(result.pop())
            