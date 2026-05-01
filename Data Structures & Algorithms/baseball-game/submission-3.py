class Solution:
    def calPoints(self, operations: List[str]) -> int:
        int_arr = []
        for op in operations:
            if op not in "CD+":
                int_arr.append(int(op))
            else:
                if op == "C":
                    int_arr.pop()
                elif op == "D":
                    int_arr.append(int_arr[-1]*2)
                elif op == "+":
                    int_arr.append(int_arr[-1] + int_arr[-2])
        return sum(int_arr)

# ops = ["1","2","+","C","5","D"]
# int_arr = []
# "1" : not in "CD+", int_arr[1]
# "2" : "", int_arr[1,2]
# "+" : "", int_arr[1,2,3]
# "C" : "", int_arr[1,2]
# "5" : "", int_arr[1,2,5]
# "D" : "", int_arr[1,2,5,10]