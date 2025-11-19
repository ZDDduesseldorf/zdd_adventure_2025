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
class Scentlab(Room):
    def run_story(self, user_items):
        if self.visited == 1:
            print("You walk into the Scentlab...What an interesting room, you think to yourself.")
            print("Suddenly, a diffuser sprays a mysterious scent into the room!")
            print("As the mist settles, you notice a shimmering pink perfume bottle on the floor.")

            perfume = Item(
                name="experimental perfume bottle",
                description="A shimmering pink perfume bottle. The scent keeps shifting.",
                movable=True
            )
            self.items.append(perfume)

        else:
            print()
        return user_items
    
    def enter_room(self, user_items, command_handler):
        self.visited += 1
        print("You step into the Scentlab.")
        user_items = self.run_story(user_items)

        while True:
            action = input(">> smell perfumes / inspect shelves / inspect perfume / leave: ").strip().lower()
            if command_handler.handle_global_commands(action):
                return user_items
            if action == "leave":
                print("You leave the Scentlab.")
                return user_items
            elif action == "smell perfumes":
                print("You smell different fragrances...floral, sweet, and something strangely metallic.")
            elif action == "inspect shelves":
                print("The shelves are full of labelled and unlabbeled bottles. Some even glow softly.")
            elif action == "inspect perfume":
                if not self.items:
                    print("There is no perfume bottle here anymore.")
                else:
                    for item in self.items:
                        print(item.description)
                        if item.movable:
                            take = input(">> Do you want to take the perfume bottle? (yes/no): ").strip().lower()
                            if take == "yes": 
                                user_items.append(item)
                                self.items.remove(item)
                                print("You took the perfume bottle.")
                            else:
                                print("You decided to leave the perfume bottle.")
            else: 
                print("Unknown Command.")
            
        
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")


ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    
}
