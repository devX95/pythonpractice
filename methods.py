def someFunc(name=""):
  '''
  Explanation
  '''
  return f"Hello {name}"

print(someFunc("Gibran"))

def myFunc(a, b, c=0):
  return sum((a, b, c)) * 0.05

print(myFunc(40, 60, 100))

def myFuncArgs(*args):
  return sum(args) * 0.05

print(myFuncArgs(40, 60, 100, 100))

def myFuncKwargs(**kwargs):
  if 'fruit' in kwargs:
    print(f'{kwargs["fruit"]}')
  elif 'veggie' in kwargs:
    print(f'{kwargs["veggie"]}')
  else:
    print('Else')

print(myFuncKwargs(fruit='apple', veggie='lettuce'))

def dblFunc(*args, **kwargs):
  print(f'I would like {args[1]} {kwargs["food"]}')

dblFunc(10, 30, fruit="orange", food="eggs")