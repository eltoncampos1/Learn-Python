question_prompts = [
    "What color are Apples?\n (a) Red/Green\n (b)Purple\n (c) Orange\n\n",
    "What color are Bananas?\n (a) teal\n (b) Purple\n (c) Yellow\n\n",
    "What color are grapes?\n (a) Purple\n (b) green\n (c) Red", 
]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_arr = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]

def runt_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


runt_test(questions_arr)