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
    
class ServerRoom(Room):
    def run_story(self, user_items):
        print("Cold air hits your face as you enter the room.")
        print("Rows of server racks line the walls, covered in blinking LEDs.")

        if self.visited == 1:
            print("You hear the loud humming of GPUs training a large language model.")
        else:
            print("The constant humming of the GPUs fills the room in the background.")

        return user_items
    
club_mate = Item("club mate", "A lukewarm caffeine beverage. Fuel for coding.", movable= True)

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
server_room = ServerRoom("server room", "A loud, cold room filled with blinking racks.", items_init = [club_mate])
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "server_room": server_room,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
