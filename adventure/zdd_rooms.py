"""This is to keep all special rooms of the ZDD."""
from main_classes import Item, Room


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

class ForgottenStudy(Room):
    def __init__(self):
        super().__init__(
            name="Forgotten Study",
            description="A dusty, sealed room with a stone altar in the center. "
                        "A locked wooden box rests quietly on it.",
            items_init=None
        )
        self.box_opened = False   # player can only solve puzzle once

    def run_story(self, user_items):
        print("\nYou enter a forgotten study. The air is stale.")
        
        # If puzzle already solved → nothing else happens
        if self.box_opened:
            print("The wooden box on the altar is already open.")
            return user_items

        print("On the altar rests a locked wooden box.")
        print("It has a rectangular indentation… it looks like it fits a small book.")
        print("(hint) Maybe something you carry matches this shape?")

        # Check if player has the old book
        has_old_book = any(x.name == "old book" for x in user_items)

        action = input("Do you want to place the old book on the box? (yes/no): ").strip().lower()

        if action in {"yes", "y"}:
            if not has_old_book:
                print("You try to place something… but you don't have the required item.")
                return user_items

            # Puzzle solved
            print("You place the old book into the indentation…")
            print("The box clicks open! Inside lies a mysterious paper.")
            self.box_opened = True

            # Remove old book
            user_items = [x for x in user_items if x.name != "old book"]

            # Give cheat sheet
            print("You obtained the 'exam cheat sheet'!")
            user_items.append(CHEAT_SHEET)

            return user_items

        else:
            print("You leave the box untouched.")
            return user_items

class ArchiveWithSecret(Room):
    def show_items(self, user_items):
        print("You inspect the archive… old folders, dust… and a LARGE BOOKSHELF?")
        print("You pull it slightly… A secret door opens to the FORGOTTEN STUDY!")
        return super().show_items(user_items)
    
# ---------------- NEW ITEM FOR ISSUE 103 -------------------
CHEAT_SHEET = Item(
    name="exam cheat sheet",
    description=(
        "A crumpled paper full of desperate last-minute notes. "
        "It reads: 'The final boss is weak against good code structure!'"
    ),
    movable=True
)
# -----------------------------------------------------------

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
