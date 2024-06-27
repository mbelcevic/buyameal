# Random Meal Buyer Selector

This script allows you to enter a list of friends' names and randomly selects one of them to buy the meal.

## How to Use

1 Run the script.
2 Follow the prompts to add names to the list.
3 The script will randomly select one person from the list to buy the meal.


## Script Explanation

### Functions

#### add_names()
This function prompts the user to enter names and adds them to a list. The user can add as many names as they want. The function returns the list of names.

Prompts:
"Enter a name to add to the list: ": Asks for a friend's name.
"Do you want to add more names? (yes/no): ": Asks if the user wants to add more names.

#### select_random_payer(names)
This function takes a list of names and randomly selects one name from the list. It then prints out the name of the person who will buy the meal.

### Main Flow
Add Names: The script calls add_names() to create a list of names.
Select Random Payer: The script calls select_random_payer(names) to randomly select and announce who will buy the meal.

