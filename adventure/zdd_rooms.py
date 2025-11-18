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

class StorageRoom(Room):
    def run_story(self, user_items):
        print("As you step inside, dust particles dance in the dim light.")
        print("It smells like old paper and rusting metal.")
        print("You see shelves packed with boxes labeled 'ZDD 2010' and 'Top Secret'.")
        
        # Kleines Interaktions-Element für die Atmosphäre
        action = input("Do you want to open one of the boxes? (yes/no): ").strip().lower()
        if action == "yes":
            print("You open a box... it's full of old cables and floppy disks. Nothing useful here.")
        else:
            print("Better not touch anything. It looks unstable.")
            
        return user_items

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
storage_room = StorageRoom("storage", "A small, dusty room filled with old boxes and forgotten equipment.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "storage_room": storage_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
