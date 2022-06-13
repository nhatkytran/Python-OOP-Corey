class Student:
  raise_value = 1.3
  total_student = 0
  # Class variables are for all instances

  def __init__(self, first_name, last_name, money):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
    # Instance variables are unique to every instance

    self.__class__.total_student += 1
  
  # Classes have attributes and methods
  
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

  def raise_money(self):
    self.money = int(self.money * self.raise_value)
    # usr self.raise_value instead of self.__class__.raise_value
    # because sometime when you need override for a unique instance


frlix = Student('Frlix', 'Tran', 1000)

#

# print(frlix.get_full_name()) # Frlix Tran
# self keyword is aytomatically passed into a function

# print(Student.get_full_name(frlix)) # Frlix Tran
# how self keyword is passed behind the scene

#

#

# print(Student.total_student) # 1

# print(Student.raise_value) # 1.3
# print(frlix.raise_value) # 1.3

# print(Student.__dict__) # ...'raise_value': 1.3,...
# print(frlix.__dict__) # {'first_name': 'Frlix', 'last_name': 'Tran', 'money': 1000}

# frlix.raise_money()
# print(frlix.money) # 1300

# frlix.raise_value = 1.5
# print(Student.raise_value) # 1.3
# print(frlix.raise_value) # 1.5
# print(frlix.__dict__)
# {'first_name': 'Frlix', 'last_name': 'Tran', 'money': 1000, 'raise_value': 1.5}
# actually create new attribute (or override) raise_value unique for frlix instance

# frlix.raise_money()
# print(frlix.money) # 1500
# new frlix instance uses its own attribute raise_value

#

#

# @classmethod and @staticmethod

class Student:
  raise_value = 1.3

  def __init__(self, first_name, last_name, money):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
  
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

  def raise_money(self):
    self.money = int(self.money * self.raise_value)
  
  @classmethod
  def set_raise_value(cls, new_value):
    cls.raise_value = new_value

  @classmethod
  def from_string_hyphen(cls, string_hyphen):

    def string_to_int(item):
      try:
        return int(item)
      except ValueError:
        return item

    items = map(string_to_int, string_hyphen.split('-'))
    return cls(*items)
  
  @staticmethod
  def is_dayoff(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return True
    return False


# There are 3 methods:
# 1. Regular method: Automatically pass 'self' as the first argument
# 2. Class method: Automatically pass 'class' as the first argument
# 3. Static method: Don't automatically pass any thing as the first argument

# Note: Use class method to set new value and use class method as constructor

# frlix = Student('Frlix', 'Tran', 1000)
# ky = Student('Ky', 'Tran', 1000)

# print(Student.raise_value) # 1.3
# print(frlix.raise_value) # 1.3
# print(ky.raise_value) # 1.3

# Instead of using Student.raise_value
# Use class method

# Student.set_raise_value(1.5)

# print(Student.raise_value) # 1.5
# print(frlix.raise_value) # 1.5
# print(ky.raise_value) # 1.5

# frlix_infor = 'Frlix-Tran-1000'
# Student.from_string_hyphen(frlix_infor)

# print(frlix.first_name) # Frlix
# print(frlix.last_name) # Tran
# print(frlix.money) # 1000
# print(type(frlix.money)) # <class 'int'>

# Use static method when you don't need to use 'self' or 'class'

# import datetime

# new_date = datetime.date(2022 ,6 ,12) # True
# new_date = datetime.date(2022 ,6 ,13) # False

# print(Student.is_dayoff(new_date))

#

#

# Inheritance and Subclasses

class Student:
  raise_value = 1.3

  def __init__(self, first_name, last_name, money):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
  
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

  def raise_money(self):
    self.money = int(self.money * self.raise_value)


class SpecialStudent(Student):
  def __init__(self, first_name, last_name, money, languages=None):
    super().__init__(first_name, last_name, money)
    # Student.__init__(self, first_name, last_name, money)
    # Use super for matainability purposes
    if languages is None:
      self.languages = []
    else:
      self.languages = languages

  def get_languages(self):
    for language in self.languages:
      print(language)


frlix = SpecialStudent('Frlix', 'Tran', 1000, ['Python', 'JavaScript'])

# frlix.get_languages()
# Python
# JavaScript

# print(isinstance(frlix, SpecialStudent)) # True
# print(isinstance(frlix, Student)) # True
# print(issubclass(SpecialStudent, Student)) # True

#

#

# dunder methods

class Student:
  raise_value = 1.3

  def __init__(self, first_name, last_name, money):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
  
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'

  def raise_money(self):
    self.money = int(self.money * self.raise_value)

  def __repr__(self):
    return f'{self.__class__.__name__}(fist_name={self.first_name}, last_name={self.last_name}, money={self.money})'

  def information(self):
    return f'{self.first_name} {self.last_name} - Money: {self.money}'
  
  __str__ = information

# Note:
# __repr__ is to be ambiguous
# __str__ is to be readable

# __repr__ dunder has the idea of indenpotance


frlix = Student('Frlix', 'Tran', 1000)

# print(repr(frlix)) Student(fist_name=Frlix, last_name=Tran, money=1000)
# print(str(frlix)) # Frlix Tran - Money: 1000