class MyList(list):
    def remove_min(self):
        self.remove(min(self))

    def remove_max(self):
        self.remove(max(self))


x = [1, 3, 5, 6, 8, 9, 3, 4]

y = MyList(x)
y.remove_min()
print(y)


class NewList(list):
    def remove_max(self):
        self.remove(max(self))

    def append_sum(self):
        self.append(sum(self))


x = NewList([1, 2, 3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()

print(x)

"""
What will this print?
Nothing: this program will never halt.
"""
