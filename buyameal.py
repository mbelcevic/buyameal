import random

def add_names():
    names = []
    # Welcome to the game
    print("Hello. Please add friends' names, and I will choose one of them randomly to buy the meal :)")
   
    while True:
        name = input("Enter a name to add to the list: ").strip()
        if name:  # Ensure that the name is not empty
            names.append(name)
        else:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        
        while True:
            more = input("Do you want to add more names? (yes/no): ").strip().lower()
            if more in ["yes", "no"]:
                break
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")
        
        if more == "no":
            break
    return names

def select_random_payer(names):
    print("Checking...")
    print("Checking...")
    print("...")
    random_index = random.randint(0, len(names) - 1)
    selected_name = names[random_index]
    print(f"{selected_name} is going to buy the meal today!")

 
    
# Add names to the list
names = add_names()

# Select and print the name of the person who will buy the meal
select_random_payer(names)
