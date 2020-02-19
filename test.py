import json
import random

number_questions = 7
points = 0
questions_made = []

def exam():
    with open('questions-2.json') as questions_file:
        data = json.load(questions_file)
        while len(questions_made) < number_questions:
            random_index = random.randint(0,len(data)-1)
            if random_index not in questions_made:
                questions_made.append(random_index)
                print('---------------------------------------------------------------')
                print(data[random_index]['question'])
                print(data[random_index]['options'])
                my_answer = raw_input('Answer: ').lower()
                if my_answer == data[random_index]['answer']:
                    points += 1

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('You have {} points'.format(points))


def main():
    exam()

if __main__ == "__main__":
    main()
