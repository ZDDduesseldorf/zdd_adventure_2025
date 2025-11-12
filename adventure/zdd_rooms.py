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

class PrinterLab(Room):
    def __init__(self, name, description):
        
        blueprint = Item(
            "3d printer blueprint", 
            "A detailed technical blueprint for a complex 3D printer.",
            movable=True
        )
        
        work_table = Item(
            "work table", 
            "A sturdy work table with various technical drawings and tools.",
            movable=False
        )
        super().__init__(name, description, [work_table, blueprint])

    def run_story(self, user_items):
        print("You see a pretty small lab with humming 3D printers...")
        print("In the corner stands a work table covered with technical drawings.")
        return user_items

        
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
printer_lab = PrinterLab("3d printer lab", "Makes sense there's a room like that here.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "printer_lab": printer_lab
}
