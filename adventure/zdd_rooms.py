"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item

fallen_key = Item(
    name="fallen key",
    description="A small metal key that must have fallen out of a shoe.",
    movable=True
)
class WalkInCloset(Room):
    def run_story(self, user_items):
        print("You enter the room, when you suddendly trip over a pair of shoes.")
        if self.visited == 1:
            self.items.append(fallen_key)
        return user_items

    def enter_room(self,user_items,command_handler):
        self.visited += 1
        print(f"you enter the {self.name}.")

        user_items = self.run_story(user_items)

        while True:
            action = input(">> inspect outfits / inspect sehlves / look around / leave: ").strip().lower()

            if command_handler.handle_global_commands(action):
                return user_items
            
            if action == "leave": 
                print(f"You leave the {self.name}.")
                return user_items
            
            elif action == "inspect outfits":
                print("Various clothes are hanging around.")

            elif action == "inspect shelves":
                print("Shelves filled with bags, boxes and accessories.")

            elif action == "look around": 
                print("A messy closet full of clothes and shoes. Something might be on the floor.") 
                user_items = self.show_items(user_items)


            else:
                print("Unknown command")


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
walk_in_closet = WalkInCloset(
    name="Walk-In Closet",
    description="A messy closet filled with clothes, shelves and many shoes."
)
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "walk_in_closet": walk_in_closet
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
