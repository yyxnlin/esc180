ret_square = 0

def parrot_trouble(talking, hour):
  if (talking == True and (hour < 7 or hour > 20)):
    return True
  return False



def sum_double(a, b):
  if (a == b):
    return a*4
  return a+b



def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  return False


def set_square(x):
  global ret_square
  ret_square = x**2
