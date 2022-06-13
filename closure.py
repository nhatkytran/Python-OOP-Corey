def outer():
  message = 'Hello World!'
  # message is free variable

  def inner():
    return message

  return inner


startCoding = outer()

# print(startCoding()) # Hello World!