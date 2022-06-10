class Student:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    # Instance variables
  
  def get_full_name(self):
    return f'{self.first_name} {self.last_name}'
# Classes have attributes and methods


frlix = Student('Frlix', 'Tran')

# print(frlix.get_full_name()) # Frlix Tran
# self keyword is aytomatically passed into a function

# print(Student.get_full_name(frlix)) # Frlix Tran
# how self keyword is passed behind the scene
