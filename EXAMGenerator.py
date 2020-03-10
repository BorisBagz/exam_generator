import json
import random
import os

"""
EXAM GENERATOR
by: boris a.
"""

# GLOBAL VARIABLES
number_questions = 50        #number of questions we want to ask
questions_made = []         #array with the index of the questions already answered
answers = []                #array with the good and given answers
json_questions = 'questions-ccsa.json'     #json file containing the questions
valid_answers = ['a', 'b', 'c', 'd']    #array with the valid options as answers
valid_exams = ['CCSA R80']
passing_score = 71

def presentation():
    print('\n\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('   |                                                |')
    print('   |         Welcome to EXAM GENERATOR v1.0         |')
    print('   |                  by: boris a.                  |')
    print('   |                                                |')
    print('    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
    user = raw_input('Your name: ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Available exams:')
    print('1.   Checkpoint CCSA - R80')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    examcode = raw_input('Choose the exam you want to take: ')
    exam_name = valid_exams[int(examcode)-1]
    return user, exam_name

def start_exam(user, exam_name):
    print('---------------------------------------------------------------')
    print('\n\nHello {0}, you\'re about to start the {1} exam.'.format(user, exam_name))

#read the json file and load it to the variable DATA
def read_json_file(json_file):
    with open(json_file) as questions_file:
        data = json.load(questions_file)
        return data

#check if the random generated number used as
#index for the questions was not already asked
#if it is indeed new, we append the question to the array questions_made
def check(my_number):
    if my_number not in questions_made:
        questions_made.append(my_number)
        return True

#generate a random number between 0 and the total number of questions in the json
#then checks if it was not asked yet
def generate(length):
    while True:
        my_number = random.randint(0,length)
        if check(my_number):
            return my_number

def print_question(data, index):
    print('\n---------------------------------------------------------------')
    print(data[index]['question'])
    print(data[index]['options'])

#check if the given answer is a,b,c or d (appears in valid_answers)
def validate_answer(my_answer):
    if my_answer in valid_answers:
        return True
    else:
        return False

#fetch the input from the user
#while true (do while loop) to check if the input is a b c or d
#in that case, add the given answer along with the good answer to the answers array
#return the given answer
#otherwise ask the option again
def answering():
    while True:
        my_answer = raw_input('Answer: ').lower()
        if validate_answer(my_answer):
            answers.append(my_answer)
            return my_answer
        else:
            print('Invalid option')

#compute the percentage of the score
def check_score(points):
    score = (points*100)/number_questions
    return score

def print_final_score(points):
    score = check_score(points)
    print('\n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|                                                                                |')
    print('|    Your final score is {0} % - You answered correctly {1} out of {2} questions.     |'.format(score, points, number_questions))
    if score >= passing_score:
        print('|                      You passed the test! Congratulations!                     |')
    else:
        print('|                 You didnt pass the test, better luck next time!                |')
    print('|                                                                                |')
    print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# def print_answers():
#     print('\nResults: ')
#     print('\t    Your Answer   Correct Answer')
#     for i in range(0,len(answers)):
#         print('Question {0} :\t{1}       |       {2}'.format(i+1, answers[i][0].upper(), answers[i][1].upper()))

#print the CORRECTIONS
#get the index found in the questions_made array
#print that question from the data, the options and the answer
def print_corrections(data):
    print('CORRECTIONS:')
    for i in range(len(questions_made)):
            index = int(questions_made[i])
            question = data[index]['question']
            options = data[index]['options']
            answer = data[index]['answer']
            print('Question {}: '.format(str(i+1)))
            print(data[index]['question'])
            print(data[index]['options'])
            print('Correct answer : {}'.format(data[index]['answer'].upper()))
            print('Your answer    : {}'.format(answers[i][0].upper()))
            print('--------------------------------------------------------')


#core of the EXAM
#fetch the data from the json, execute the CORE while the amount of asked questions
#in questions_made is the same as the number_questions we want to ask
#pick a random question (no repetition)
#fetcht the answer from the user and compute the score
def exam(user, exam_name):
    points = 0
    data = read_json_file(json_questions)
    length = len(data)-1
    start_exam(user, exam_name)
    while len(questions_made) < number_questions:
        random_index = generate(length)
        print_question(data, random_index)
        good_answer = data[random_index]['answer']
        my_answer = answering()
        if my_answer == good_answer:
            points += 1
    print_final_score(points)
    choice_answers = raw_input('\nDo you want to see the corrections of the test? (Y/N)')
    if(choice_answers.upper() == 'Y'):
        print_corrections(data)

def main():
    #if we're on linux we clear the screen when launching the script
    if os.name == "posix":
        os.system("clear")
    user, exam_name = presentation()
    exam(user, exam_name)

if __name__ == '__main__':
    main()
