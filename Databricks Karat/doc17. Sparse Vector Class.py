import math
class SparseVector:
    def __init__(self, size):
        self.vector = [0 for _ in range(size)]
        self.size = size

    def set(self, index, value):
        try:
            self.vector[index] = value
        except IndexError:
            print('Index out of range')

    def get(self, index):
        try:
            return self.vector[index]
        except IndexError:
            print('Index out of range')
            return None

    def add(self, vector):
        if vector.size != self.size:
            print('Length not equal')
            return

        new_vector = SparseVector(self.size)
        for i in range(self.size):
            new_vector.set(i, vector.get(i) + self.get(i))

        return new_vector

    def dot(self, vector):
        if vector.size != self.size:
            print('Length not equal')
            return

        result = 0
        for i in range(self.size):
            result += vector.get(i) * self.get(i)
        return result

    def cosine(self, vector):
        if vector.size != self.size:
            print('Length not equal')
            return 0

        return self.dot(vector) / (self.norm() * vector.norm())

    def norm(self):
        result = 0
        for i in range(self.size):
            result += self.vector[i] * self.vector[i]
        return math.sqrt(result)

    def __str__(self):
        return str(self.vector)

v1 = SparseVector(5)
v1.set(0, 4.0)
v1.set(1, 5.0)
v2 = SparseVector(5)
v2.set(1, 2.0)
v2.set(3, 3.0)
v3 = SparseVector(2)

print(v1.add(v2))
print(v3.add(v3))
print(v1.dot(v2))
print(v1.dot(v3))
print(v1.cosine(v2))
print(v1.cosine(v3))