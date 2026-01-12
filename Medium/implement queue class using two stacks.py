                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []    # all inserts go here
        self.out_stack = []   # all removals come from here

    def enqueue(self, x):
        # Step 1: insert into first stack
        self.in_stack.append(x)

    def _shift_stacks(self):
        # Step 2: move elements only when out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())  

    def dequeue(self):
        # Ensure correct order before removal
        self._shift_stacks()
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack.pop()

    def peek(self):
        # Look at front element without removing
        self._shift_stacks()
        if not self.out_stack:
            raise IndexError("Queue is empty")
        return self.out_stack[-1]

    def is_empty(self):
        return not self.in_stack and not self.out_stack
