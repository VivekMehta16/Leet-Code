class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack =[]
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2-num1)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                num1, num2 = stack.pop(), stack.pop()
                #Truncate toward zero as per RPN spec
                result = int(float(num2) / num1)
                stack.append(result)
            else:
                stack.append(int(c))
        return stack[0] 