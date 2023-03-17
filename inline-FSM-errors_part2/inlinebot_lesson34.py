"""
classmethod()
@classmethod
factory
"""

class A:
    x = 5
    y = 2

    def add(sefl, a: int, b: int) -> int: #пример 1
        return a+b
    
    @classmethod #пример 2
    def sub(cls):
        return cls.x - cls.y

"""Пример 1"""

instance = A()

A.add = classmethod(A.add)

print(A.add(5,3))

"""Пример 2"""

print(A.sub())


"""Пример 3"""

class B:
    x = 5
    y = 2

    def __init__(self, a: float) -> None:
        self.a = a

    @classmethod
    def sub(cls):
        return cls(13)
    
print(B.sub().__dict__)