class Game:
    def __init__(self):
        self.intro()
    
    def intro(self):
        print("Welcome to the Haunted House Adventure!")
        print("You find yourself at the entrance of a dark and eerie house.")
        print("What would you like to do?")
        self.first_choice()

    def first_choice(self):
        choice = input("Do you want to (1) enter the house or (2) leave? (1/2): ")
        if choice == '1':
            self.enter_house()
        elif choice == '2':
            print("You decided to leave the haunted house. Game over!")
        else:
            print("Invalid choice, please try again.")
            self.first_choice()

    def enter_house(self):
        print("\nYou step inside the house. It's dark and dusty.")
        print("You see a staircase leading up and a door to your left.")
        self.second_choice()

    def second_choice(self):
        choice = input("Do you want to go (1) upstairs or (2) through the door? (1/2): ")
        if choice == '1':
            self.upstairs()
        elif choice == '2':
            self.through_door()
        else:
            print("Invalid choice, please try again.")
            self.second_choice()

    def upstairs(self):
        print("\nYou climb the creaky stairs.")
        print("At the top, you find a mysterious glowing room.")
        choice = input("Do you want to (1) enter the room or (2) go back down? (1/2): ")
        if choice == '1':
            print("Inside the room, you find a treasure chest filled with gold! You win!")
        elif choice == '2':
            self.enter_house()
        else:
            print("Invalid choice, please try again.")
            self.upstairs()

    def through_door(self):
        print("\nYou open the door and step into a kitchen.")
        print("Suddenly, the door slams shut behind you!")
        choice = input("Do you want to (1) search for a way out or (2) look for food? (1/2): ")
        if choice == '1':
            print("You find a window and escape the haunted house! You win!")
        elif choice == '2':
            print("While looking for food, a ghost appears! You are trapped. Game over!")
        else:
            print("Invalid choice, please try again.")
            self.through_door()

if __name__ == "__main__":
    Game()
