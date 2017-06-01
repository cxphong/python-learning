import time

class TestException(Exception):
   def __init__(self, arg):
      self.args = arg

try:
	raise TestException("Test error")
except TestException as e:
	print (e.args)
