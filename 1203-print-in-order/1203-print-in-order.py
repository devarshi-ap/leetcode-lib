import threading

class Foo:
    def __init__(self):
        self.e1 = threading.Event()
        self.e2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.e1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.e1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.e2.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()