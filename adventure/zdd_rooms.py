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

class YourRoom(Room):
    def run_story(self, user_items):
        print("You enter your room. It's calm... but something feels off.")

        
        if "laptop" in [x.name for x in user_items]:
            print("Your laptop suddenly lights up in your backpack.")
            print("A huge wall of unfinished tasks appears on the screen.")
            print("The stress hits you instantly... it's overwhelming.")

          
            action = input("Do you want to smash the laptop out of frustration? (yes/no): ").strip().lower()

            if action == "yes":
                print("You slam the laptop on the ground. The screen shatters into pieces.")
                print("Strangely enough... you feel a bit better.")
                
                return [x for x in user_items if x.name != "laptop"]

            print("You hold yourself back and close the laptop.")
            print("You're stressed... but proud of your self-control.")

        else:
            print("You look around. Without your laptop, the room feels strangely quiet.")
        
        return user_items

    
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
your_room= YourRoom("your Personal Room", "This is your Personal space ...you are not alone work is waiting for u")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    
}
