import random
import time
from itertools import product
from progress.bar import Bar

def characters_possible()->str:
  lowercases = "abcdefghijklmnopqrstuvwxyz"
  uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  digits = "0123456789"
  specials = "()[]:;!"
  return f"{lowercases}{uppercases}{digits}{specials}"

def generate_pwd(length:int) -> str:
  """
  Generate a random password according to the length given
  """
  characters = characters_possible()
  result = ""
  for i in range(0, length):
      result += random.choice(characters)
  print(result)


def bruteforce(pwd:str) -> None:
  """
  Try to brute force a password
  """
  characters = characters_possible()
  bar = Bar('Processing', max=len(pwd)+1)
  for i in range(len(pwd) + 1):
    bar.next()
    for attempt in product(characters, repeat = i):
      if ''.join(attempt) == pwd:
        bar.finish()
        return ''.join(attempt)

def possible_combination(pwd:str):
  """
  Computes the number of possible combinations for a password of length x.
  Calculation : 
  Sum of all the possible characters, that is a total of 69.
  For example, a 6-character password will have 69 with an exponent of 10, 
  i.e. a total of 2 446 194 060 654 759 801 possibilities.
  """
  characters = characters_possible()
  possibility=len(characters) ** len(pwd)
  print(possibility)
  return possibility

def time_for_bruteforce(pwd:str)-> int:
  """
  Calculate the time to brute force a password
  """
  start = time.time()
  print(bruteforce(pwd))
  end = time.time()
  print(f"Execution time: {end - start}s")
  return end - start

def average_of_time_bruteforce(pwd: str, test: int)->int:
  """
  Calculate the time to brute force a password for x time
  """
  list_of_time = []
  for i in range(test):
    list_of_time.append(time_for_bruteforce(pwd))
  average = sum(list_of_time)/len(list_of_time)
  print(f"The average is {'%.3f' % average} seconds for {test} test")
  return average
