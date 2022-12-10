

class Point:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def function1(self, num):
        while num > 1:
            num = self.function2(num)
            p = Point(num)

            if self.head is None:
                self.head = p
            else:
                cur = self.head

                while cur.next:
                    cur = cur.next

                cur.next = p

        c = self.head
        n = []
        while c:
            n.append(str(c.value))
            c = c.next
        print(' -> '.join(n))


    def function2(self, x):
        y = x / 2
        return y


new_l = List()
num = 50
new_l.function1(num)