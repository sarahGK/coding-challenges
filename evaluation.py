import re

# ---DESCRIPTION ----#

__author__ = 'Xin G Kelly'

#This is the code in Python3 to evaluate a mathematical expression of arbitrary length, with any digit and symbols: '( )','+','-','*' and '/' .
#The program takes a string as an input and print out the value of the evaluated expression.We assume that all input is well-formed and that multiplication is never implied. The program will print the output as a float number in the screen.
#

# --- HELPER FUNCTIONS ---#

# This function deals with the strings without brackets and calculates the results for operators '*' and '\'
# It returns a list only with numbers, '+' and '-'
# Based on the priorities of the operators, it should alawys be called before add_sub function

def mul_div(result):
  if len(result) == 1 :
    return result[0]
  else :
    
    index = 0
    last = []
    while index < len(result) :
      ch = result[index]

      if isinstance(ch,float) or ch == '+' or ch == '-':
        last.append(ch)
        index = index + 1
      else:

        if ch == '*':
          number = last.pop() * result[index+1]
        elif ch == '/':
          number = last.pop() / result[index+1]

        last.append(number)
        index = index + 2

    return last

# This function deals with the list only with numbers, '+' and '-'.
# It return a float number.
# Based on the priorities of the operators, it should only be called after mul_div function.

def add_sub(last):
  if isinstance(last,float):
    return last
  if len(last) == 1:
    return last[0]
  else:
    
    evaluation = last[0]
    index = 1
    while index < len(last) -1 :
      if last[index] == '+':
        evaluation = evaluation + last[index+1]
      elif last[index] == '-':
        evaluation = evaluation - last[index+1]
      index = index + 2

  return evaluation

# This function uses the stack data structure to evaluate the string between pairs of brackets.
# For each ')' in str, it will evaluate the string within its closet '(' using mul_div and add_sub functions.
# It returns a list without brackets in it.

def removebracket(str,result):
  for x in str:
    if x == ')' :

      bracket = []
      # pop items out of the stack until the last one is '('
      while True:
        ch=result.pop()
        if ch == '(':
          break
        else:
          bracket.append(ch)
      # reverse the list to get the right order of the mathematical expression
      bracket.reverse()
      result_muldiv = mul_div(bracket)
      result.append(add_sub(result_muldiv))
    else:
      result.append(x)

  return result

# ---MAIN FUNCTION ---#

# This function takes the initial string as input and returns a float number as the final evaluation of the string.
# It uses regular expression to find all the numbers in the string and store them as float in the list and read through each charactor.
# For "()", it uses removebracket function to evaluate the string in between and for other 4 operators, store them as string in the list.


def evaluate(str):

# INITIALIZATION
# start and end is the beginning and the end indices of numbers in the string
# result is the list of float number and operators read from the input string
# substr is the string after the slide window sized of the current found number 
  start = 0
  end = 0
  result = []
  substr = str

  while True:
    if end >= len(substr) :
      break;

    substr = substr[end:]
    # search the first number in substr
    number = re.search('\d+\.?\d*',substr)
    # If no number left
    if number is None:
      result = removebracket(substr,result)
      break
    else:
      start,end = number.span()
      # For all the charactors between two numbers
      if start > 0:
        prev = substr[0:start]
        result = removebracket(prev,result)

      result.append(float(substr[start:end]))

  result_muldiv = mul_div(result)
  return add_sub(result_muldiv)

# --- RESULTS --- #

if __name__ == '__main__':
  str = '2*(3+(4+(5*6+7)*8))-1'
  print(evaluate(str))
  str = "1+2-3*4/5"
  print(evaluate(str))
  str = "4+6"
  print(evaluate(str))
  str = "(4+6)*3"
  print(evaluate(str))
  str = "2+(2.5)*2"
  print(evaluate(str))
  str = "2+(((2.5+2)*2+3)*4+5)-5/(2-3)"
  print(evaluate(str))
