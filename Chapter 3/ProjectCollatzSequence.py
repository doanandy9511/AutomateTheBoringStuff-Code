
def collatz(num):
    if num % 2 == 0:
        num = num // 2
        print(num)
        return num
    else:
        num = 3 * num + 1
        print(num)
        return num

try:
    print('Enter number:')
    inputNum = int(input())
    while True:
        inputNum = collatz(inputNum)
        if inputNum == 1:
            break
except ValueError:
    print('Invalid input. Please enter an integer.')