"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
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

class ServerRoom(Room):
    def run_story(self, user_items):
        print("You enter the room but realize the power is out.")
        print("You see the emergency lights shining on the room's equipment.")

        # time.sleep adds time breaks to the text
        if "cooling fan" in [x.name for x in user_items]:
            time.sleep(4)
            print("\nYou are startled by a heatwave.\nWhat is happening?")
            print("The server room is overheating!!!\n")
            time.sleep(4)
            print("You remember that you picked up the cooling fan earlier in the archive.")
            print("However, there is a problem... there are 4 USB ports but only one works.\n")
            time.sleep(5)
            print("In order to figure out which one to use you have to solve the following riddle:\n")
            time.sleep(3)

            riddle = "'My friends are named One, Two, and Three.\n We’re all standing together in a line.'\nHow many people are standing in a line?\n"
            for char in riddle:
                print(char, end="", flush=True)
                time.sleep(0.08)

            user_inp = input("What is the answer?:\n>")
            # checking user input
            if user_inp == "4":
                print("You hook up the portable USB fan to the 4th port.")

                dramatic = "..."
                for char in dramatic:
                    time.sleep(1.2)
                    print(char, end="", flush=True)
                time.sleep(1)           
                   
                print("\nCool air is starting to cool down the server room.")
                print("Mission successful! You stopped the system from overheating.")
                return [x for x in user_items if x.name != "cooling fan"]
            
            print("Oh no...You used the wrong port.")
            print("The USB fan is damaged and of no use anymore..")
            return [x for x in user_items if x.name != "cooling fan"]
        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
server_room = ServerRoom("server_room", "This is the massive server room of the ZDD.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "server_room": server_room
    # "my_room_key": my_room
}
