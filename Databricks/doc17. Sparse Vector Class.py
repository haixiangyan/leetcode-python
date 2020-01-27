import math
class SparseVector:
    def __init__(self, size):
        self.vector = [0 for _ in range(size)]
        self.size = size

    def set(self, key, value):
        try:
            self.vector[key] = value
        except IndexError:
            print('Index out of range')

    def get(self, key):
        try:
            return self.vector[key]
        except IndexError:
            print('Index out of range')
            return None

    def add(self, vector):
        if vector.size != self.size:
            print('Length not equal')
            return 0

        new_vector = SparseVector(self.size)
        for i in range(self.size):
            new_vector.set(i, self.vector[i] + vector.get(i))
        return new_vector

    def dot(self, vector):
        if vector.size != self.size:
            print('Length not equal')
            return 0

        result = 0
        for i in range(self.size):
            result += self.vector[i] * vector.get(i)
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
