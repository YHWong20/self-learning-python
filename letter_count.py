# Iterative Method
def count(letter: str, word: str):
  letter_count = 0
  for char in word:
    if letter == char:
      letter_count += 1
  return letter_count

print(count("p", "apple")) # yields 2


# Recursive Method
def count(letter: str, word: str):
  if len(word) == 0:
    return 0
  elif letter == word[0]:
    return 1 + count(letter, word[1:])
  return count(letter, word[1:])

print(count("t", "trouble in terrorist town")) # yields 4
