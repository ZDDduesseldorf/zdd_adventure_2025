"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random


class ToiletCellar(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        # issue #44: Initialize password and sheet as Item
        self.password = f"{random.randint(10000, 99999)}"
        self.password_sheet = Item(
            "password sheet",
            f"A paper towel with numbers: {self.password}",
            movable=False
        )
        self.sheet_available = True
    
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        # Check by name; if the book is present, drop it (story event)
        washed_hands = False
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            # Remove book from inventory
            user_items = [x for x in user_items if x.name != "old book"]
            washed_hands = True
        
        # issue #44: Password sheet with hands washed/unwashed (depending on book)
        if self.sheet_available:
            if washed_hands:
                print("\nYour hands are still wet. There's a paper towel dispenser on the wall.")
            else:
                print("\nThere's a paper towel dispenser on the wall.")
            
            action = input("Pull out a towel? (yes/no): ").strip().lower()
            if action in {"yes", "y"}:
                self.password_sheet.describe()
                print("It bursts into flames.")
                self.sheet_available = False
            elif action in {"no", "n"}:
                print("You leave the dispenser alone.")
        
        return user_items


class MachineRoom(Room):
    def __init__(self, name, description, toilet_ref):
        super().__init__(name, description)
        # issue #43: Initialize machine room attributes
        self.fixed = False
        self.toilet = toilet_ref
    
    def run_story(self, user_items):
        if self.fixed:
            print("The machines are running.")
            return user_items
        
        print("All machines are off? Wait, there's a terminal on this screen, maybe...?")
        print("\nTERMINAL: ENTER 5-DIGIT PASSWORD")
        
        code = input("Code: ").strip()
        
        if len(code) == 5 and code.isdigit():
            if code == self.toilet.password:
                print("The password was correct. The power is back on.")
                self.fixed = True
            else:
                print("Wrong password! I should get a new one.")
                self.toilet.password = f"{random.randint(10000, 99999)}"
                self.toilet.password_sheet = Item(
                    "password sheet",
                    f"A paper towel with numbers: {self.toilet.password}",
                    movable=False
                )
                self.toilet.sheet_available = True
        else:
            print("Invalid format.")
        
        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
machine_room = MachineRoom("machine room", "Large machines... they should be generating power.", toilet_cellar)

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "machine_room": machine_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
