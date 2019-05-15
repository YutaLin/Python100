import os
import time


def main():
    content = 'Welcome to python world...'
    while True:
        os.system('cls')  # os.system('clear')
        print(content)
        # sleep 200 mileseconds
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()