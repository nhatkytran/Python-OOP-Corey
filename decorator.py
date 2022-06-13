# Decorator with Class
class Decorator:

  def __init__(self, original_function):
    self.original_function = original_function

  def __call__(self, *args, **kwargs):
    print(f'Class Decorator ran before {self.original_function.__name__}')
    return self.original_function(*args, **kwargs)


@Decorator
def logger():
  print('Logger function')


# logger()
# Class Decorator ran before logger
# Logger function


# Decorator with Loggin module
def logger(original_function):
  import logging
  logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

  def wrapper_function(*args, **kwargs):
    logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
    return original_function(*args, **kwargs)

  return wrapper_function;


@logger
def sum(a, b):
  return a + b


# print(sum(10, b=20)) 30
# INFO:root:Ran with args: (10,), and kwargs: {'b': 20} ('./sum.log)


# Decorator with timer function
def timer(original_function):
  import time

  def wrapper_function(*args, **kwargs):
    start = time.time()
    result = original_function(*args, **kwargs)
    end = time.time()
    print(f'{original_function} ran in {end - start}s')
    return result

  return wrapper_function


@timer
def sum_long_time(a, b):
  return a + b


# print(sum_long_time(10, 20))
# <function sum_long_time at 0x106997010> ran in 9.5367431640625e-07s
# 30


# Chain decorator
def new_logger(original_function):
  def wrapper_function(*args, **kwargs):
    print('Function new_logger ran')
    return original_function(*args, **kwargs)

  return wrapper_function


@timer
@new_logger
def greeting():
  print('Hello')
  return 'Greeting'


# print(greeting())
# Function new_logger ran
# Hello
# <function new_logger.<locals>.wrapper_function at 0x1074a4c10> ran in 4.100799560546875e-05s
# Greeting

# Note: <function new_logger.<locals>.wrapper_function at 0x1074a4c10>
# Unexpected - side effect


# wraps decorator
from functools import wraps

def timer(original_function):
  import time

  @wraps(original_function)
  def wrapper_function(*args, **kwargs):
    start = time.time()
    result = original_function(*args, **kwargs)
    end = time.time()
    print(f'{original_function} ran in {end - start}s')
    return result

  return wrapper_function


def new_logger(original_function):
  @wraps(original_function)
  def wrapper_function(*args, **kwargs):
    print('Function new_logger ran')
    return original_function(*args, **kwargs)

  return wrapper_function


@timer
@new_logger
def greeting():
  print('Hello')
  return 'Greeting'


# print(greeting())
# Function new_logger ran
# Hello
# <function greeting at 0x109f98dc0> ran in 4.315376281738281e-05s
# Greeting