class MyQueue:

    def __init__(self):
        self.s1 = [] # input stack (for push)
        self.s2 = [] # output stack (for peep/pop)

    def push(self, x: int) -> None:
        # push to top (end of s1)
        self.s1.append(x)

    def pop(self) -> int:
        # pop from top (move elements s1 > s2, inverting order, pop from s2)
        # s1=[1,2,3], s2=[] --> s1=[], s2=[3,2,1]
        # if s2 has any elements, pop from there first
        self.move_elements()
        return self.s2.pop()

    def peek(self) -> int:
        # peek from top
        self.move_elements()
        return self.s2[-1]

    def empty(self) -> bool:
        # queue is effectively = s1 + s2[::-1] (hence, queue is empty if both are empty)
        return not self.s1 and not self.s2

    def move_elements(self) -> None:
        if len(self.s2) == 0: # s2 (output stack) is empty, continue repopulating with number dump
            while self.s1:
                self.s2.append(self.s1.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()