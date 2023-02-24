#!usr/bin/env python3
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

print(f"{trivia['question']}")
print(f"A. {html.unescape(trivia['correct_answer'])}")
print(f"B. {html.unescape(trivia['incorrect_answers'][0])}")
print(f"C. {html.unescape(trivia['incorrect_answers'][1])}")
print(f"D. {html.unescape(trivia['incorrect_answers'][2])}")
correct_answer = "A"
user_answer = input("What is the correct answer above? ('A','B','C',or 'D')\n> ")
if user_answer == correct_answer:
    print("You are correct!")
else:
    print("Wrong!")
