
def eggs(someParameter):
    print(id(someParameter))
    someParameter.append('Hello')

def main():
    spam = [1, 2, 3]
    print(id(spam))
    eggs(spam)
    print(spam)

if __name__ == '__main__':
    main()
