import math
# Add any extra import statements you may need here
import string

DIGITS = string.digits
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
    from functools import partial
    process = partial(process_char, rotation_factor=rotation_factor)
    return ''.join(list(map(process, input_str)))

def process_char(c, rotation_factor):
    if c.isalnum():
        return process_alphanumeric_char(c, rotation_factor)
    return c

def process_alphanumeric_char(c, rotation_factor):
    if c.isdigit():
        return process_digit(c, rotation_factor)
    if c.isupper():
        return process_upper(c, rotation_factor)
    if c.islower():
        return process_lower(c, rotation_factor)

def process_digit(c, rotation_factor):
    n = len(DIGITS)
    index = DIGITS.index(c)
    new_index = calculate_new_index(index, rotation_factor, n)
    return DIGITS[new_index]


def process_upper(c, rotation_factor):
    n = len(UPPERCASE)
    index = UPPERCASE.index(c)
    new_index = calculate_new_index(index, rotation_factor, n)
    return UPPERCASE[new_index]

def process_lower(c, rotation_factor):
    n = len(LOWERCASE)
    index = LOWERCASE.index(c)
    new_index = calculate_new_index(index, rotation_factor, n)
    return LOWERCASE[new_index]


def calculate_new_index(index, rotation_factor, n):
    return (index + rotation_factor) % n


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
