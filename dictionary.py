import json

# Load data from json file
data = json.load(open("data.json"))

# User question
question = "What would you like to know? (enter X to quit): \n"

# User Input
user_input = input(question)

while (user_input != "X"):
    try:
        print(data[user_input])
    except Exception:
        print("Error: Invalid input!")
    # Print results
    print("\n")
    user_input = input(question)
    