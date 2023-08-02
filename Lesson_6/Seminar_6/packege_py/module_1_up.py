import random
from sys import argv


def guess_the_num(min_num, max_num, attempt):
    # min_num, max_num, attempts = input('Enter min,max and attempts: ').split()
    # min_num, max_num, attempts = int(min_num), int(max_num), int(attempts)
    num = random.randint(min_num,max_num)
    if attempt != 0:
        while attempt>0:
            try:
                player = int(input(f'You have {attempt} attempts. Enter num: '))
            except:
                print('Need int!')
                attempt-=1
                continue
            if player > num:
                print("Number is smaller.")
            elif player < num:
                print("Number is bigger.")
            elif player == num:
                return True
            elif attempt ==0:
                return False
            attempt-=1


if __name__ == "__main__":
    min_num,max_num,attempts = input('Enter min,max and attempts: ').split()
    min_num,max_num,attempts = int(min_num),int(max_num),int(attempts)
    print(guess_the_num(min_num,max_num,attempts))
