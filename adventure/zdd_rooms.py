"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import time


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        # Check by name; if the book is present, drop it (story event)
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            return [x for x in user_items if x.name != "old book"]
        return user_items

class SecurityRoomSecondFloor(Room):
    def run_story(self, user_items):
        paper_note = Item("paper note", "a note that gives you a hint for the puzzle in the security room")

        print("You enter a warm and gloomy room. A huge screen glows on the wall.")
        print("In the room you find a console, a chair and a trashcan in the corner")

        # Player can choose if they want to interact with items in the room or immediately try out to guess the answer.
        first_choice = input("Do you want to take a look around first? (y/n): ")

        if first_choice == "n":
            print("You walk directly to the console.")
            print("Try to enter the correct color order.")

            input_order = []
            # Only this combination gives access to security footage.
            correct_order = ["red", "green", "blue"]

            while True:
                press_button = input("Press a button (green/blue/red): ")

                if press_button in ["green", "blue", "red"]:
                    # Adds the chosen color to the empty list.
                    input_order.append(press_button)
                else:
                    print("Not a valid button. Try again.")
                    continue
                
                if input_order == correct_order:
                    print("Access granted to security footage!")
                    break

                if len(input_order) == 3 and input_order != correct_order:
                    print("Access denied: wrong passcode.")
                    # If the answer is incorrect, the player will have to try again until they guess it right.
                    input_order = []


        else:
            look = input("Look into the trashcan? (y/n): ")
            if look == "y":
                print("You find a small paper sheet inside the trashcan.")
                take_and_read = input("Take the note and read what it says? (y/n): ")
                if take_and_read == "y":
                    user_items.append(paper_note)
                    print("You take it out. It says: First it's warm. In the end it's cold.")
                    print("Could this be a hint?")
                
                else:
                    sit = input("You decide to ignore the content of the paper sheet. You see an empty chair. Do you want to sit on it? (y/n): ")
                    if sit == "y":
                        print("You sit down. Nothing happens. Really, nothing.")
                        time.sleep(3)
                        print("Maybe you should do something...")
            
            else:
                print("You ignore the trashcan.")

            print("You go back to the console. Try to enter the correct color order.")

            # Same principle as before, player has to guess the correct order.
            input_order = []
            correct_order = ["red", "green", "blue"]

            while True:
                press_button = input("Press a button (green/blue/red): ")

                if press_button in ["green", "blue", "red"]:
                    input_order.append(press_button)
                else:
                    print("Not a valid button. Try again.")
                    continue
                
                if input_order == correct_order:
                    print("Access granted to security footage!")
                    break

                if len(input_order) == 3 and input_order != correct_order:
                    print("Access denied: wrong passcode.")
                    input_order = []

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
security_room = SecurityRoomSecondFloor("security room", "a warm and gloomy room with a big screen and a console")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "security_room": security_room
    # "my_room_key": my_room
}
