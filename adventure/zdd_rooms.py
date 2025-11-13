"""This is to keep all special rooms of the ZDD."""
from main_classes import Room


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

class SecretRoom(Room):
    def run_story(self, user_items):
        print("You've entered the secret room.")  
        print("In front of you are three drawers: A, B and C.")
        print("One of the drawers may contain something useful...")
        # Player chooses a drawer
        choice = input("Which drawer do you want to open? (A/B/C): ").strip().lower()
        if choice == "b":
            # Player finds the pen in drawer B
            print("You open drawer B and find an invisible ink pen!")
            pen = Item("invisible ink pen", "A pen that can reveal secret messages.")
            user_items.append(pen)
            print("You take the pen and notice a nearby note...")
            print("At first, the note seems blank.")
            # Player deceides whether to use the pen or not
            reveal_choice = input("Do you want to use the pen and see the message? (yes/y to reveal): ").strip().lower()
            if reveal_choice in ["yes", "y"]:
                print("The pen glows and the hidden message appears:")
                print(" 'Soon you are going to be trapped in a room!'")
            else:
                # Player chooses not to reveal the message
                print("You leave the note blank. Maybe you weren't the chosen one.")
        else:
            # Player finds nothing in drawers A and C 
            print("That drawer is empty. Maybe try a diffrent one.")
        return user_items

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

secret_room = SecretRoom("secret_room", "A hidden room with mysterious drawers.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "secret_room": secret_room 
}
