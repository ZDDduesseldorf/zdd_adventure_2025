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

class your_room (Room):
    def run_story (self,user_items): 
        print ("you're now in your room and see ur laptop on the table")
        print("The laptop screen is still glowing faintly... maybe you should inspect it.")

        action = input("Type ""Inspect"" to check the Laptop or Press Enter to ignore it.").strip().lower()
        if action == "inspect":
            print("You open the laptop. Oh no...")
            print("A list of unfinished homework pops up!")
            print("ZDD Adventure Project -Tasks to complete:")
            print("1) Implement YourRoom story")
            print("2) Add task list interactions")
            print("3) Don't forget to commit & push your work!")

            print("\nThe overwhelming list makes you feel extremely stressed and tense...")
            print("U slowley feel the urge to smash the Laptop to the ground..")
            action2 = input ("If u want to break it type (yes/no)").strip().lower()
            if action2== ("yes"):
                 print("In a sudden burst of frustration, you slam the laptop shut so hard the screen cracks.")
                 print("The laptop is now completely broken... but weirdly, you feel a bit better.")
            else : 
                print("You take a deep breath and decide NOT to break the laptop.")
                print("you're such a calm Person maybe next time, now do ur work than...")

        return user_items
    
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
your_room= your_room("your Personal Room", "This is your Personal space ...you are not alone work is waiting for u")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "your_room": your_room,
}
