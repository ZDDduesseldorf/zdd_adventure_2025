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
    
class JanitorsCloset(Room):
    def run_story(self, user_items):
        print(f"You've entered the {self.name} {self.visited} time(s).")
        # Check by name; if the key is present, open the closed
        if "small key" in [x.name for x in user_items]:
            print("You open the locked cabinet, you see the private goods of the janitor.")
            print("You decide to act morally, so you lock it again and decide to throw the key away...")
            # Remove small key from inventory
            return [x for x in user_items if x.name != "small key"]
        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
locked_cabinet = Item("locked cabinet", "There is a locked cabinet. It's locked. It looks like it needs a small key.", movable=False)
janitors_closet = JanitorsCloset("janitors closet", "The private goods of the janitor... Interesting", locked_cabinet)

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "janitors_closet": janitors_closet
}
