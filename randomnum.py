import random
def bang_game():
    random_num = random.randrange(100, 300)
    number = str(random_num)
    flag = 0
    i = 0
    print("enter a number between 100 to 300")
    print("You have 3 chances")
    print("Try to guess what it is.")
    print("************************************")
    while (i < 3):
        print("\n#Guess:", i, end=" ")
        guess = input("\nenter a number between 100 to 300  ")
        if (guess == number):
            flag = 1
            break
        else:
            for j in range(0, 3):
                if number[j] == guess[j]:
                    print("same", end=" ")
                elif guess[j] in number:
                    print("wrong position", end=" ")
                else:
                    print("incorrect", end=" ")
            pass
        i = i + 1
    if flag == 1:
        print("\ncorrect")
        print("answer is ", number)
    else:
        print("\nbetter luck next time")
        print(" answer is  ", number)
    play_again()
def play_again():
    ask = input("Do you want to play again(Y/N): ")
    if ask == 'y':
        bang_game()
bang_game()
