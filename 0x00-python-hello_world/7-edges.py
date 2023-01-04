#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

demo = word[1:-1]
print('demo(1:-1): ', demo)
print('word[-1]: ', word[-1])
# 0 1 2 3 4 5 6 7 8
# H o l b e r t o n

# -1 -2 -3 -4 -5 -6 -7 -8 -9
# n  o  t  r  e  b  l  o  H
