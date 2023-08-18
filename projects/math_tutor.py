from random import randrange as r
from time import time as t
# import modules
# ask how many questions user wants
no_questions = int(input('How many questions do you want?: '))
max_num = int(input('Highest number used in practice?: '))
# set score start at zero
score = 0
answer_list = []
start = t()
# loop through number of questions
for q in range(no_questions):
    num_one, num_two = r(1, max_num + 1), r(1, max_num + 1)
    ans = num_one * num_two
    user_ans = int(input(f'{num_one} x {num_two} = '))
    answer_list.append(f'{num_one} X {num_two} = {ans} you:{user_ans}')

    if ans == user_ans:
        score += 1
    end = t()

print(f'Thank you for playing! \nYou got {score} out of {no_questions} \
      ({round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds \
        ({round((end-start)/no_questions,1)}seconds/question)')

for a in answer_list:
    print(a)

# show user the question
# capture answer and modify user score
# output final score
