
# String-Based Examination Answer Evaluation

answer_key = "ABCDAB"
student_answers = input("Enter your 6 answers: ").upper()

correct = 0
wrong = 0
unanswered = 0

if len(student_answers) == 6:

    for i in range(6):

        if student_answers[i] == answer_key[i]:
            correct += 1

        elif student_answers[i] == "-":
            unanswered += 1

        else:
            wrong += 1

    marks = (correct * 2) - (wrong * 0.5)

    print("\n--- Examination Result ---")
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Unanswered Questions:", unanswered)
    print("Final Marks:", marks)

else:
    print("Please enter exactly 6 answers.")
