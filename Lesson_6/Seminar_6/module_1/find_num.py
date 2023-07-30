import random

def gess_the_num(min,max,attempt):
    if attempt ==0:
        data = int(input('Wrong data. Enter the number of attempts: '))
        return gess_the_num(min,max,data)
    num = random.randint(min,max)
    if attempt != 0:
        while attempt>0:
            player = int(input(f'You have {attempt} attempts. Enter num: '))
            if player > num:
                print("Number is smaller.")
            elif player < num:
                print("Number is bigger.")
            elif player == num:
                # print("Congratulations!You win!")
                return True
            elif attempt ==0:
                # print('Sorry,you loose.')
                return False
            attempt-=1


if __name__ == "__main__":
    min_num,max_num,attempts = input('Enter min,max and attempts: ').split()
    min_num,max_num,attempts = int(min_num),int(max_num),int(attempts)
    print(gess_the_num(min_num,max_num,attempts))