"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random

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

class SmallCasinoCornerSecondFloor(Room):
    def run_story(self, user_items):
        lucky_token = Item("lucky token", "a small token with a four-leaf clover engraved on it", movable=True)
        print("You entered the small casino corner. There's a slot machine...")
        counter = 0
        
        while True:
            if counter == 0: # Attempt Counter
                action = input("Do you want to try your luck? (yes/no): ").strip().lower()
            else:
                action = input("Do you want to try again? (yes/no): ").strip().lower()
            
            if action in {"yes", "y"}:
                counter += 1
                win_number = random.randint(1, 5) # Random Number between 1 and 5 (20% Win rate)
                if win_number == 1:
                    user_items.append(lucky_token) # Add Lucky Token to inventory
                    print("Ding ding! You win a shiny Lucky Token!")
                    print(f"Attempt {counter}")
                    print("---- Lucky Token ----")
                    lucky_token.describe()
                    break
                else:
                    print("Nothing happens... maybe next time.")
                    
            elif action in {"no", "n"}:
                print(f"That's a great decision. Don't gamble!")
                break
            else: 
                print("Please answer with yes or no!")
        return user_items

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
small_casino_corner = SmallCasinoCornerSecondFloor("small casino corner", "A slot machine, a small chair and a flickering neon sign that says 'CASINO'.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "small_casino_corner": small_casino_corner
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
