# randomQuizGenerator.py - creates quizzes w questions and answers
# in random order, along with the answer key
import random
from pathlib import Path

def main():
    # the quiz data. Keys are states and values are their capitals
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


    path = Path.cwd() / 'Chapter 9 - Reading and Writing Files' / 'Capitals Quizzes'
    # generate 35 quiz files
    for quizNum in range(35):
        # create the quiz and answer key files
        with open(path / f'capitalsquiz{quizNum+1}.txt', 'w') as quizFile, \
             open(path / f'capitalsquiz_ans{quizNum+1}.txt', 'w') as ansKeyFile:
            # header for quiz
            quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quizFile.write(f"{' '*20}State Capitals Quiz (Form{quizNum+1})\n\n")

            # shuffle the order of the states
            states = list(capitals.keys())
            random.shuffle(states)
            
            # loop through all 50 states, making a question for each
            for questionNum in range(50):
                # get the correct and incorrect answers
                correctAnswer = capitals[states[questionNum]]
                wrongAnswers = list(capitals.values())
                wrongAnswers.remove(correctAnswer)
                answerOptions = random.sample(wrongAnswers, 3)
                answerOptions.append(correctAnswer)
                random.shuffle(answerOptions)

                # write the question and the answer options to the quiz file
                quizFile.write(f'{questionNum+1}. What is the capital of {states[questionNum]}?\n')
                for i in range(4):
                    quizFile.write(f"   {'ABCD'[i]}. {answerOptions[i]}\n")
                quizFile.write('\n')

                # write the answer key to a file
                ansKeyFile.write(f"{questionNum+1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

if __name__ == '__main__':
    main()