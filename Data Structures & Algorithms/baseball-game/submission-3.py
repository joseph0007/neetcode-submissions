class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                b = scores.pop()
                a = scores.pop()
                c = int(a or 0) + int(b or 0)
                scores.extend([a,b,c])
            elif op == "C":
                scores.pop()
            elif op == "D":
                a = scores.pop()
                b = int(a or 0)*2
                scores.extend([a,b])
            else:
                scores.append(op)
        result = 0
        for score in scores:
            result += int(score or 0)
        return result