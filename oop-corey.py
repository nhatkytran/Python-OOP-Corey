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