import random
import string
import math
from abc import ABCMeta, abstractmethod
# s1 = 'hello world'
# print(s1, end='')

#####################################
s1 = '\'hello world\''
# s2 = '\n\\hello world!\\\n'
# print(s1, s2, sep=',', end='')

#####################################
# def fib_(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a
#
# def main():
#     for val in fib_(20):
#         print(val)
#
# if __name__ == '__main__':
#     main()

#####################################
# def gen_code(num):
#     number_ = ''.join([str(index) for index in range(10)])
#     string_ = string.ascii_lowercase[:26]
#     together_ = number_ + string_
#
#     code_ = ''
#     for index in range(num):
#         code_ += together_[random.randint(0, len(together_) - 1)]
#
#     return code_
#     # return ''.join(code_)
#
#
# if __name__ == '__main__':
#     print(gen_code(12))

##################################################
'''
@setter     adjust the value of a property
@property   fetch the value of a property
'''
# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property       # fetch property info
#     def name(self):
#         return self.name
#
#     @property       # fetch property info
#     def age(self):
#         return self.age
#
#     @age.setter     # update to a new value of property
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('can not watch anything')
#         else:
#             print('can watch anything you like')
#
# def main():
#     person = Person('FEI TENG', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     print(person._age)
#     print(person._name)
#     # this is not allowed, as property name is not under @setter
#     # person.name = 'Yuting Li'
#
# if __name__ == '__main__':
#     main()

###############################################
# class Person(object):
#
#     __slots__ = ('_name', '_age', '_gender')
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('watch under PG')
#         else:
#             print('watch whatever you like')
#
# def main():
#     person = Person('FEI TENG', 12)
#     person.play()
#     person._gender = 'Male'
#
# if __name__ == '__main__':
#     main()
#
####################################################
'''
staticmethod: 
            Dynamic method is used to process the attributes of an OBJECT. E.g., you calculate the area of a triangle. 
            However, some processes are not directly associated with an OBJECT, like you check the feasibility of 
            constructing a triangle before you calculate its area. In this sense, this marginal processes are considered
            as static method. USE @staticmethod
'''
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and a + c > b and c + b > a
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter()/2
#         return math.sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))
#
# def main():
#     a, b, c = (3, 4, 5)
#     if Triangle.is_valid():
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         print(t.area())
#     else:
#         print('can not construct a triangle')
#
# if __name__ == '__main__':
#     main()

###########################################################
'''
super class:    the class that will be inherited
sub class:      the class that inherit super class
'''
# class Person(object):
#
#     def __init__(self, name, age):
#         self._age = age
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         print(f'{self._name} is playing')
#
#     def watch_av(self):
#         if self._age >= 18:
#             print(f'{self._name} is watching')
#         else:
#             print(f'{self._name} can not watch')
#
# class Student(Person):
#
#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade
#
#     @property
#     def grade(self):
#         return self._grade
#
#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade
#
#     def study(self, course):
#         print(f'{self._name} is studying {course}')
#
# class Teacher(Person):
#
#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title
#
#     @property
#     def title(self):
#         return self._title
#
#     @title.setter
#     def title(self, title):
#         self._title = title
#
#     def teach(self, course):
#         print(f'{self._title} {self._name} is teaching {course}')
#
#
# def main():
#     stu = Student('A', 15, '11th')
#     stu.study('math')
#     stu.watch_av()
#     t = Teacher('B', 28, 'Prof.')
#     t.teach('math')
#     t.watch_av()
#
# if __name__ == '__main__':
#     main()

#############################################################
'''
poly-morphism
'''
class Pet(object, metaclass=ABCMeta):

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print(f'{self._nickname} says Wang...')

class Cat(Pet):
    def make_voice(self):
        print(f'{self._nickname} says Mia....')

def main():
    pets = [Dog('wang cai'), Cat('katie'), Dog('Da huang')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()

    
