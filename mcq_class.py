class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

qn_lst = [
  "What Colour are Blueberries?\n1) Blue\n2) Green\n3) Purple\n\n",
  "What is 5 + 10?\n1) 13\n2) 15\n3) 20\n\n",
  "Who is Queen Elizabeth?\n1) Queen of England\n2) Queen of Spain\n3) Queen of France\n\n",
  "How many members are in Twice?\n1) 8\n2) 10\n3) 9\n\n"
]

qns = [
  Question(qn_lst[0], "1"),
  Question(qn_lst[1], "2"),
  Question(qn_lst[2], "1"),
  Question(qn_lst[3], "3")
]

def test(qns):
  score = 0
  for question in qns:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  return f"You scored {str(score)}/{str(len(qn_lst))}. Well done!"
      

print(test(qns))
