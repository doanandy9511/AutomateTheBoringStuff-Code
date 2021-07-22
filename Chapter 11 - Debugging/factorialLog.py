import logging

def main():
    logging.basicConfig(level=logging.DEBUG, 
       format='%(asctime)s - %(levelname)s - %(message)s')
    logging.disable(logging.CRITICAL) # disables LOGGING
    logging.debug('Start of program')
    print(factorial(5))
    logging.debug('End of program')

def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug(f'End of factorial {n}')
    return total

if __name__ == '__main__':
    main()
