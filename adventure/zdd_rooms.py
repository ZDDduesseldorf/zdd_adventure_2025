"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item


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

class ComputerLab(Room):
    '''This room simulates a creepy computer lab where the screens behave oddly.
    The player can choose to inspect the computers, which may trigger an
    encounter with an "evil AI". Having the "python cheat sheet" enables
    an extra branch where the player can "defeat" the AI and gain a keycard.'''
    def run_story(self, user_items):
        # Announce the room atmosphere and ask the player whether to inspect.
        print("The screens flicker, showing lines of code and strange symbols.\nYou feel a strange energy in the room, like the screens are alive.")
        user_input = input("Do you want to further inspect the computers? (yes/no): ").strip().lower()

        if user_input == "yes":
            # Enter the AI encounter. If the player has a Python cheat sheet,
            # they get an extra choice to attempt to defeat the AI.
            print("As you approach the screens, they suddenly go dark, and a voice appears from the speakers.\nIts the voice of an evil AI!\n"
                  "It tells you that you are lucky it cant reach you through the screens and warns you to leave immediately.")
            if "python cheat sheet" in [x.name for x in user_items]:
                # Player has the cheat sheet -> can choose to fight the AI.
                print("You clutch your Python cheat sheet tightly, feeling reassured by your coding knowledge.")
                user_input = input("Do you want to leave the room or will you dare to defeat the evil AI? (leave/defeat):").strip().lower()

                if user_input == "defeat":
                    # Successful defeat: add the ZDD keycard to inventory.
                    print("Using your coding knowledge and the Python cheat sheet, you manage to outsmart the evil AI!\n"
                        "You write a quick script that disables the AI and restores the screens to normal.\n"
                        "Congratulations! You have defeated the evil AI and saved the computer lab!\n"
                        "Finally feeling safe, you decide to look around the room. There is a ZDD keycard on one of the desks, which you take with you.")
                    user_items.append(Item("ZDD keycard", "A keycard that might open some doors in the ZDD.", movable=True))
                    
                    return user_items
                elif user_input == "leave":
                    # Player chooses to leave after seeing the AI.
                    print("You decide it's best to leave the room while you still can.")
                    return user_items
                else:
                    # Any other response leads to a hurried exit.
                    print("Indecision costs you dearly. You leave the room hastily, feeling uneasy.")
                    return user_items
            else:
                # Player lacks the cheat sheet -> must leave.
                print("Without any coding knowledge, you feel vulnerable and decide it's best to leave immediately. If only you had a Python cheat sheet...")
                return user_items
            
        elif user_input == "no":
            # Player chooses not to inspect the computers.
            print("You decide not to risk it and leave the room safely.")
            return user_items
        
        # Default: no change to inventory/state.        
        return user_items
    
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
computer_lab = ComputerLab("computer lab", "A Room filled with computer screens, which have flickering lights")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "computer_lab": computer_lab
}
