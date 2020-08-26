x = (i for i in range(5))
x.__next__()  # manually moving the iterator with dunder method
next(x)  # manually moving the iterator
next(x)

for i in x:
    print(i)


################################################################

class range_examp:
    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val


for i in range_examp(5):
    print(i)


################################################################

def range_gen(end):
    current = 0
    while current < end:
        yield current
        current += 1
