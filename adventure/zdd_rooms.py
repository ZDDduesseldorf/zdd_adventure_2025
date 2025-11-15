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
        print("You see three drawers labeled A, B, and C.")

        choice = input("Which drawer do you open? (A/B/C): ").strip().lower()

        if choice == "b":
            print("You found an invisible ink pen inside drawer B!")
        else:
            print("This drawer is empty.")
        
        return user_items
    


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
secret_room = SecretRoom("secret_room", "A mysterious room with three drawers labeled A, B, and C.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "secret_room": secret_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
