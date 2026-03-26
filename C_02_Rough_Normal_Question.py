import random

# Checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):

    # If any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # If the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # If the number needs to be between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # Check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer isn't too low...
            if low is not None and response < low:
                print(error)

            # Check the integer isn't too low...
            elif high is not None and response > high:
                print(error)

            # If response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

print("✖️➕ Welcome to the best math quiz of the decade! ➖➗")
wanted = string_checker("\nDo you want a question? ")

while wanted == "yes":

    # Find secret variable
    alphabet = ("a","b","c","y","x") # Just to make it look nice
    constant = random.randint(-10,10)
    if constant == 0:
        constant = 1
    variable = random.randint(1,10)
    times_variable = random.randint(2,5)
    answer = variable * times_variable + constant
    placeholder = random.choice(alphabet)

    # allow user to work it out

    if constant <= 0:
        constant *= -1
        user_answer = int_check(f"\nIf {times_variable}{placeholder} - {constant} = {answer}, what is '{placeholder}'? ",
                                low=1, exit_code="xxx")
    else:
        user_answer = int_check(f"\nIf {times_variable}{placeholder} + {constant} = {answer}, what is '{placeholder}'? ",
                  low= 1, exit_code="xxx")

    if user_answer == "xxx":
        break
    if user_answer == variable:
        print("\nYou win!")
    else:
        difference = variable - user_answer
        if difference <= 0:
            difference *= -1
        print(f"\nYou were {difference} away... The answer was {variable}, not {user_answer}")

    again = string_checker("\nDo you want to play again? ")
    if again == "no":
        break