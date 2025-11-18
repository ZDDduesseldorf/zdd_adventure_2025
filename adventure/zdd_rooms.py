"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item



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


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# ------------------- Gravity Lab -------------------
class GravityLab(Room):
    def run_story(self, user_items):
        print("You float upward and hit the ceiling!")
       
        note = next((i for i in self.items if i.name == "Note"), None)
        if note and any(x.name == "Grabber Arm" for x in user_items):
            note.movable = True
        return user_items

gravity_lab = GravityLab(
    "gravity_lab",
    "A teaching room with inverted gravity. You float on the ceiling.",
    items_init=[Item("Note", "A note on the ceiling table. Too far to read unless you have the Grabber Arm.")]
)



# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "gravity_lab": gravity_lab

    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
