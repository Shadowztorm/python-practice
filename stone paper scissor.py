# Stone, Paper, Scissor game
import random

comp_list=["Stone","Paper","Scissor"]

chances=1
user_score=0
cpu_score=0

print("-----------------------------------------")
print("Welcome to Stone, Paper and Scissor game!")
print("-----------------------------------------")

while chances <= 10:
    user_input = input("Stone\t Paper\t Or \t Scissor? \n")
    user_input=user_input.capitalize()
    CPU = random.choice(comp_list)
    # print(CPU)

    if user_input == CPU:
        print(f"You choose {user_input}\nComputer choose {CPU}\n Thats a tie.\n")
    elif user_input=="Stone" and CPU=="Paper":
        print(f"You choose {user_input}\nComputer choose {CPU}\n CPU wins.\n")
        cpu_score+=1
    elif user_input=="Stone" and CPU=="Scissor":
        print(f"You choose {user_input}\nComputer choose {CPU}\n You win.\n")
        user_score=user_score+1
    elif user_input=="Paper" and CPU=="Scissor":
        print(f"You choose {user_input}\nComputer choose {CPU}\n CPU wins.\n")
        cpu_score=cpu_score+1
    elif user_input=="Paper" and CPU=="Stone":
        print(f"You choose {user_input}\nComputer choose {CPU}\n You win.\n")
        user_score+=1
    elif user_input=="Scissor" and CPU=="Stone":
        print(f"You choose {user_input}\nComputer choose {CPU}\n CPU wins.\n")
        cpu_score+=1
    elif user_input=="Scissor" and CPU=="Paper":
        print(f"You choose {user_input}\nComputer choose {CPU}\n You win.\n")
        user_score+=1
    else:
        print("Invalid Input")
        continue


    print("Chances left {}\n".format(10 - chances))
    chances += 1

    if chances > 10:
        print("Game Over!\n")
print("-----------------------------------------")
print("Here's the Final Score")
print("-----------------------------------------")
print(f"Your Score {user_score}\nComputers Score {cpu_score}\n")
if user_score > cpu_score:
    print("Your the WINNER!\n")
elif cpu_score > user_score:
    print("Computer is WINNER!\n")
elif cpu_score == user_score:
    print("Its a TIE\n")
else:
    print("Error in game\n")
print("-----------------------------------------")