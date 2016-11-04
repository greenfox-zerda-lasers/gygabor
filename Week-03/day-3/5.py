# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack:

    def __init__(self):
        self.rep = []
        numb = 0
        rep = []

    def size(self):
        return (len(self.rep))

    def push(self, numb):
        self.rep += [numb]

    def pop(self):
        numb = self.rep[-1]
        rep = self.rep[:-1]
        self.rep = rep
        return numb

repo = Stack()
repo.push(4)
repo.push(1)
repo.push(2)
repo.push('a')

print(repo.size())
print(repo.pop())
print(repo.pop())
print(repo.size())
