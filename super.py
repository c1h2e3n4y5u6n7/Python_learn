# class Person():
#     def __init__(self):
#         print('我是Peson的__init__构造方法')
#
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         print('我是Student的__init__构造方法')
# stu = Student()
#
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3
b = B()
b.add(2)
print(b.n)
