from Question import Question

question_prompts = [
    "Where is Statue of Liberty located?\n (a)NY (b)NJ (c)Ca (d)Fl\n",
    "How many states in the US\n (a)43 (b)50 (c)51 (d)49\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
            answer= input(question.prompt)
            if answer.lower() == question.answer:
                score+= 1
            elif answer.lower() not in "abcd":
                print("Invalid entry")


    print("You got "+ str(score)+ "/"+ str(len(questions))+ " correct")

run_test(questions)
