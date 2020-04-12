"""
Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.stack = []

    def push(self, x: int) -> None:
        # case 1 - if stack is empty
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
        else:
            raise Exception("Empty stack")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStackConstantSpace:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minElement = None
        self.stack = []

    def push(self, x: int) -> None:

        if not self.stack:
            self.stack.append(x)
            self.minElement = x
        elif x >= self.minElement:
            self.stack.append(x)
        else:
            self.stack.append(2 * x - self.minElement)
            self.minElement = x

    def pop(self) -> None:
        if not self.stack:
            return
        y = self.stack.pop()
        if y <= self.minElement:
            self.minElement = 2 * self.minElement - y

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            if top < self.minElement:
                return self.minElement
            return top
        return -1

    def getMin(self) -> int:
        if self.minElement is not None:
            return self.minElement
        return -1