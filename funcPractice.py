def lesser_of_two_evens(a, b):
  if a % 2 == 0 and b % 2 == 0:
    print(min((a,b)))
  else:
    print(max((a,b)))

lesser_of_two_evens(2, 5)

def old_mcdonald(name):
  print(name.capitalize()[:3] + name[3:].capitalize())

old_mcdonald('macdonald')

def master_yoda(sentence):
  print(" ".join(sentence.split()[::-1]))

master_yoda('We are ready')

def almost_there(num):
  if  90 <= num <= 110 or 190 <= num <= 210:
    print('True')
  else:
    print('False')

almost_there(194)

def has_33(nums):
  for index, x in enumerate(nums):
    if x == 3:
      if len(nums) > index + 1 and nums[index + 1] == 3:
        return True
      else:
        continue
  return False

print(has_33([1, 1, 1, 3]))

def paper_doll(text):
  return "".join([letter*3 for letter in text])

print(paper_doll('help'))

def blackjack(a, b, c):
  total = sum((a, b, c))
  if total <= 21:
    return total
  if 11 in (a, b, c) and total >= 21:
    return total - 10
  else:
    return('BUST')

print(blackjack(9, 9, 11))

def summer_69(nums):
  total = 0
  add = True
  for x in nums:
    while add:
      if x != 6:
        total += x
        break
      else:
        add = False
    while not add:
      if x != 9:
        break
      else: 
        add = True
        break
  return total

print(summer_69([1, 3, 5, 6, 9, 11]))

def spy_game(nums):
  code = [0, 0, 7, 'x']
  for x in nums:
    if x == code[0]:
      code.pop(0)
  return len(code) == 1

print(spy_game([0, 2, 4, 5, 0, 7, 5]))

def count_primes(num):
  primes = [2]
  x = 3
  while x <= num:
    for y in primes:
      if x % y == 0:
        x += 2
        break
    else:
      primes.append(x)
      x += 2
  return primes

print(count_primes(100))