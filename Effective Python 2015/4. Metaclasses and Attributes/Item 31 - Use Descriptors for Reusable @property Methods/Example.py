"""
Things to Remember
Reuse the behavior and validation of @property methods by defining your own descriptor classes.
Use WeakKeyDictionary to ensure that your descriptor classes don¡¯t cause memory leaks.
Don¡¯t get bogged down trying to understand exactly how __getattribute__ uses the descriptor protocol for getting and setting attributes.
"""

class Homework(object):
    def __init__(self):
        self._grade = 0
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value
        
galileo = Homework()
galileo.grade = 95


class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
    
    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        
    @property
    def writing_grade(self):
        return self._writing_grade
    
    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)    # repeated 
        self._writing_grade = value
    
    @property
    def math_grade(self):
        return self._math_grade
    
    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)    # repeated 
        self._math_grade = value
        
#=>
from weakref import WeakKeyDictionary        
class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
            self._values[instance] = value
            
class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print('First ', first_exam.writing_grade, 'is right')
print('Second', second_exam.writing_grade, 'is right')

