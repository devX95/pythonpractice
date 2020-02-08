def func(): 
  return 1

one = func
print(one())

# def hello(name="Gibran"):
#   print("The hello() function has been called")

#   def greet():
#     return "\t This is the greet() function"
  
#   def welcome():
#     return "\t This is the welcome() inside hello"

#   print("I am going to return a function")

#   if name == "Gibran":
#     return greet
#   else:
#     return welcome

# myfunc = hello("Gib")

# print(myfunc())

def hello():
  return 'Hi Gibran'

def other(some_def_func):
  print('Other code runs here')
  print(some_def_func())

other(hello)

def new_decorator(original_func):
  def wrap_func():
    print('Some extra code, before the original function')
    original_func()
    print('Some extra code, after the original function')

  return wrap_func

@new_decorator
def func_needs_dec():
  print('I want to be decorated')

func_needs_dec()