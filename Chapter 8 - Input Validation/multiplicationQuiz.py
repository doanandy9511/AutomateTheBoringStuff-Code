import pyinputplus as pyip
import random, time

def main():
    numQuestions = 10
    correctAnswers = 0
    for questionNum in range(numQuestions):
        # generate two random nums
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

        prompt = f'#{questionNum+1}: {num1} x {num2} = '

        try:
            # correct answers handled by allowRegexes
            # wrong answeres handled by blockRegexes,
            #  along with custom message
            pyip.inputStr(prompt, allowRegexes=[rf'^{num1*num2}$'],
                          blockRegexes=[(r'.*', 'Incorrect!')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            # Run this block if no exceptions are raised
            print('Correct!')
            correctAnswers += 1
        time.sleep(1) # pause for 1s to allow user to see result
    print(f'Score: {correctAnswers} / {numQuestions}')

if __name__ == '__main__':
    main()