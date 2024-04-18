
import random

def main():
    min_num = int(input("Please enter the minimum value. ---> "))
    max_num = int(input(f"Please enter a number greater than {min_num}. ---> "))
    
    if(min_num < max_num):
        random_num = create_randomNum(min_num, max_num)

    else:
        print("\nThe generation failed. Please input again.\n")
        main()

    print(f"Please input your guessed number between {min_num} and {max_num}.")
    guess_the_number(random_num)

def create_randomNum(min_num, max_num):
    print("\n--- Generation of random numbers is complete. ---\n")
    randomNum = random.randint(min_num, max_num)
    #print("random number is ", randomNum)

    return randomNum

def guess_the_number(random_num):
    times = int(input("How many attempts will you make? ---> "))
    print(f"\nAnswer correctly within {times} times.\n")
    print("              --- Game start! ---\n")
    print("                      ↓")

    for i in range(1, times+1):
        answer = int(input("Guess the generated numbers. ---> "))

        if (answer == random_num):

            print("            ↓")
            print("\n    ------------------ ")
            print("   | Congratulations! |")
            print("    ------------------ \n")
            break

        elif (times-i == 0):
            print("                      ↓\n")
            print("                ^^^^^^^^^^^^^")
            print("                  Game Over  ")
            print("                ^^^^^^^^^^^^^\n")

        else:
            print("                      ↓")
            print("\nWrong answer -> The remaining count is", times-i, "times\n")
            print("                      ↓")
        
main()