letter_A = """
   o
  o o
 o o o
o     o
"""
letter_B = """
o o o 
o o o
o  o o
o  o o
"""
letter_C = """
o o o
o
o
o o o
"""
letter_D = """
o o o
o    o
o    o
o o o
"""
letter_E = """
o o o
o
o o o
o
o o o
"""
letter_F = """
o o o
o
o o o
o
o
"""
letter_G = """
o o o o
o
o   o o
o o o o
"""
letter_H = """
o     o
o     o
o o o o 
o     o
o     o
"""
letter_I = """
o o o
  o
  o
o o o
"""
letter_J = """
    o
    o
o   o
o o o 
"""
letter_K = """
o  o
o o
o o
o  o 
"""
letter_L = """
o
o
o
o o o
"""
letter_M = """
o o o   o o o
o   o   o   o
o   o o o   o
o           o
"""
letter_N = """
o o o   o
o   o   o
o   o   o
o   o o o
"""
letter_O = """
o o o
o   o
o   o
o o o
"""
letter_P = """
o o o
o o o
o 
o 
"""
letter_Q = """
o o o
o   o
o   o
o o o o
"""
letter_R = """
o o o
o o o
o o
o  o
"""
letter_S = """
o o o
 o
   o
o o o
"""
letter_T = """
o o o
  o
  o
  o 
"""
letter_U = """
o   o
o   o
o   o
o o o
"""
letter_V = """
o  o
o  o
o  o
 o 
"""
letter_W = """
o   o   o
o   o   o
o   o   o
o o o o o
"""
letter_X = """
o   o
 o o
  o
 o o
o   o
"""
letter_Y = """
o   o
 o o
  o
  o
"""
letter_Z = """
o o o
   o
  o
 o o o
"""
digit_0 = """
 o o
o   o
o   o
o   o
 o o 
"""
digit_1 = """
o o o 
o   o
    o
    o
o o o o o 
"""
digit_2 = """
o o o o 
o     o
     o
    o
o o o o o
"""
digit_3 = """
o o o o
      o
o o o o
      o
o o o o
"""
digit_4 = """
o   o
o   o
o o o
    o
    o
"""
digit_5 = """
o o o 
o
o o o
     o
o o o
"""
digit_6 = """
  o
 o
o o o  
o    o
 o o 
"""
digit_7 = """
o o o o
     o
    o
   o
  o   
"""
digit_8 = """
o o o
o   o
o o o
o   o
o o o 
"""
digit_9 = """
o o o
o   o
o o o
    o
o o o
"""

big_letters = [letter_A, letter_B, letter_C, letter_D, letter_E, letter_F, letter_G, letter_H, letter_I,
               letter_J, letter_K, letter_L, letter_M, letter_N, letter_O, letter_P, letter_Q, letter_R,
               letter_S, letter_T, letter_U, letter_V, letter_W, letter_X, letter_Y, letter_Z]
latin_lowercase = 'abcdefghijklmnopqrstuvwxyz'
big_digits = [digit_0, digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9]
digits = "0123456789"

text = input("text: ")
for symbol in text:
    symbol = symbol.lower()
    if symbol in latin_lowercase:
        index = latin_lowercase.index(symbol)
        letter = big_letters[index].replace('o', '.')
        print(letter, end='')
    elif symbol in digits:
        index = digits.index(symbol)
        digit = big_digits[index].replace('o', '.')
        print(digit, end='')
    elif symbol == ' ':
        print()
        print()
    else:
        print(symbol)
print()

