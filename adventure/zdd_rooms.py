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

class FlowerMeadow(Room):
    def run_story(self, user_items):
        print("You step into a peaceful indoor meadow.")
        print("Warm light shines from above, and soft grass covers the floor.")
        print("The whole place feels calming and quiet.")
        return user_items
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
flower_meadow_room = FlowerMeadow("flower meadow", "A calming indoor meadow filled with warm light and soft grass.")


# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "flower_meadow": flower_meadow_room,
}
