import pyinputplus as pyip
import random, time

def main():
    numQuestions = 10
    
    correctAnswers = 0
    for i in range(numQuestions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        prompt = f'#{i+1}: {num1} x {num2} = '

        try:
            pyip.inputStr(prompt=prompt,allowRegexes=[rf'^{num1*num2}$'],
                          blockRegexes=[(r'.*', 'Incorrect!')],
                          limit=3, timeout=8)
        except pyip.RetryLimitException:
            print('Out of tries!')
        except pyip.TimeoutException:
            print('Out of time!')
        else:
            print('Correct!')
            correctAnswers += 1
        time.sleep(1)
    print(f'Score {correctAnswers}/{numQuestions}')

if __name__ == '__main__':
    main()