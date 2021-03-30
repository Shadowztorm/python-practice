
dict = {"Human":"a living thing",
      "Maths":"the study of numbers, shapes, and space using reason and usually a special system of symbols and rules for organizing them.",
      "Connection":"a relationship in which a person or thing is linked or associated with something else.",
      "Conjunction":"the action or an instance of two or more events or things occurring at the same point in time or space.",
      "Mutable": "Changable eg. Lists",
      "Immutabe":"Unchangable eg.Tuples"
      }

print("Welcome to my Dictionary")

user_input = input("Enter a word to get its meaning: \t")

if user_input in dict:
    print(f"{user_input}: {dict[user_input]}")
else:
    print("No such word is in our dictionary")

