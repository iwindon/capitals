import random

from colorama import init, Fore, Style

init(autoreset=True)

# Define a dictionary with state-capital pairs
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",

}

def quiz_game():
    print(f"{Fore.BLUE}{Style.BRIGHT}Welcome to the U.S. State Capitals Quiz!")
    print("Type 'exit' to quit the game.\n")

    while True:
        # Choose a random state
        state, capital = random.choice(list(state_capitals.items()))

        # Ask the user for the capital
        user_input = input(f"{Fore.WHITE}{Style.BRIGHT}What is the capital of {state}? ").strip().lower()

        if user_input == "exit":
            print("Thanks for playing! Goodbye.")
            break
        elif user_input == capital.lower():
            print(f"{Fore.GREEN}{Style.BRIGHT}Correct!\n")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Oops! The correct answer is {capital}.\n")

if __name__ == "__main__":
    quiz_game()
