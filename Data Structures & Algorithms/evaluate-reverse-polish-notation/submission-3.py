class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            print(stack)
            if c.isdigit() or (len(c) > 1 and c[0] == '-'):
                stack.append(int(c))
                continue

            a = stack.pop()
            b = stack.pop()

            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(b - a)
            elif c == '*':
                stack.append(a * b)
            else:
                stack.append(int(b/a))

        ans = stack.pop()
        return ans
        