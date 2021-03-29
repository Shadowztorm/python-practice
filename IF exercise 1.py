## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

Qs=int(input("Select any 1 question/exercise: 1 or 2\n"))

if Qs == 1:
    user_input = input("Enter city name to know which country it belongs: \n")
    if user_input in india:
        print(f"The city {user_input} belongs in India")
    elif user_input in pakistan:
        print(f"The city {user_input} belongs in Pakistan")
    elif user_input in bangladesh:
        print(f"The city {user_input} belongs in Bangladesh")
    else:
        print("There is no such city in our list")

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For
# example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it
# should print "They don't belong to same country"
elif Qs==2:
    print("Comparision between two city if they belong in same country")
    user1=input("Enter 1st city name: ")
    user2= input("Enter 2nd city name: ")

    if user1 and user2 in india:
        print(f"{user1} and {user2} both belong to India")
    elif user1 and user2 in pakistan:
        print(f"{user1} and {user2} both belong to Pakistan")
    elif user1 and user2 in bangladesh:
        print(f"{user1} and {user2} both belong to Bangladesh")
    else:
        print(f"{user1} and {user2} both belong to different country")

else:
    print("Invalid option")