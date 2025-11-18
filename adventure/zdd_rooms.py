"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item
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

class InfiniteLibrary(Room):

    def run_story(self, user_items):
        if self.visited == 1:
            print("You decided to wander around the Library but there seems to be no end...")
            time.sleep(1)
            print("It feels overwhelming, so you decide to do a simple task to calm your mind.")
        else:
            print("You find yourself once again in the Infinite Library.")
        ##Giving Users the exact Input option, so there is no confusion
        print("\nYou may:")
        print("  - read book")
        print("  - observe shelves")
        print("  - inspect lights")
        print("  - or simply none")
        #Takes User Input
        while True:
            action = input("What do you do? ").strip().lower()

            if action == "read book":
                self.read_book()
            elif action == "observe shelves":
                self.observe_shelves()
            elif action == "inspect lights":
               self.inspect_lights()
            elif action == "none":
                break
            else: print("That doesnt seem to work here")
              

        return user_items


    def read_book(self):
        print("You take a random book from the shelves and decide to read it")
        print("The Fallen Angel is written on the Cover")
        time.sleep(1)
        print("It is something you have never seen before, it tells the story about an yet Unkown Archangel")
        time.sleep(3)
        print("Opening the Book the Pages turn themselves, too fast to even read")
        print("You try to focus but youre just not fast enough so you try to hold the paper by Force")
        print("THE BOOK SHUTS and you get a very bad feeling so you put it back")


    def observe_shelves(self):
        print("You walk along the shelves, trying to understand their structure...")
        time.sleep(1)
        print("But the rows of books seem to shift subtly when you're not looking.")
        time.sleep(1)
        print("Some shelves look old and dusty, while others seem impossibly new.")
        print("You reach out to touch a book—")
        time.sleep(1)
        print("—but your fingers brush through the air, as if the shelf moved away.")
        time.sleep(1)
        print("You feel watched, but nothing is there.")


    def inspect_lights(self):
        print("You've decided to take a closer look at the lights ")
        print("They seem warm and in some strange way soft")
        action = input("Do you want to touch the nearest light? (yes/no)").strip().lower()
        if action in {"yes","y"}:
            print("You reacht out carefully")
            time.sleep(2)
            print("You touch the lights and a sudden warmth goes through your body")
            print("It felt like a moment, you feel oddly rested but when you check for the time you realise you've been touching the light for over 2 hours")
            print("You feel well rested now")
        else: print("Its probably better who knows what these lights are made of ")
    

    
        

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
floating_feather= Item("floating_feather","A glowing feather floating upwards like the rules of gravity do not apply to it, it doesnt seem to do anything useful", movable = True,)
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
infinite_library = InfiniteLibrary("infinite_library", "Infinite Hallways in all directions, bookshelfs over bookshelfs, Books float in the Air and pages turn themselves",[floating_feather])
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "infinite_library" : infinite_library
}
