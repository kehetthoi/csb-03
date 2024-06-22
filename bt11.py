# with open("nhap.txt", "a") as f:
#     nhanenter = 0
#     while nhanenter < 2:
#         a = input("nhap tu: ")
#         if a == "":
#            nhanenter += 1
#         else:
#             nhanenter = 0
#             f.write(a + "\n")
# with open("nhap.txt", "r") as f:
#     print(f.read())


# from datetime import datetime
# with open('log.txt', 'a') as f:
#     while True:
#         a = input('nhap tu: ')
#         if not a:  
#             break
#         f.write(datetime.now().strftime("%d/%m/%y %H:%M:%S.%f") + '\n')
#         f.write(a + '\n')
# with open('log.txt', 'r') as f:
#     print(f.read())


def load_questions(filename):
    questions = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip(): 
                question, answer = line.strip().split(',')
                questions.append((question.strip(), answer.strip()))
    return questions
def run_quiz(questions):
    correct_answers = 0
    print("Give the correct answers to get points.")
    for i, (question, correct_answer) in enumerate(questions, start=1):
        print(f"{i}. {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            correct_answers += 1
    total_questions = len(questions)
    print(f"\n== You scored {correct_answers}/{total_questions} points ==")
question_file = "question-bank.txt"
questions = load_questions(question_file)
run_quiz(questions)







