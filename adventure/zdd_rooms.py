"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item



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
    

class GamingRoom(Room):

    florians_laptop = Item(
            "Florian's laptop",
            "A laptop with a sticker 'Property of Florian'. It looks intact but won't turn on.",
            movable=False  
        )
        
    other_laptops = Item(
            "pile of laptops",
            "A stack of various student laptops. Most have dead batteries or broken screens.",
            movable=False
        )
        
     
    def run_story(self, user_items):

        # What happens when the room is visited once

        if self.visited == 1:
            print("\nDozens of laptops line the metal shelves.")
            print("Some are neatly organized, others thrown in hastily during the evacuation.")
            print("One laptop on the main desk catches your eye - it has a name tag: 'FLORIAN'")

        # # What happens when the room is visited twice
        
        elif self.visited >= 2:
            print("\nThe laptop storage room. Florian's laptop sits on the desk.")
        
        
        has_charger = any(item.name == "laptop charger" for item in user_items) # checks if the player has / has found the laptop charger 
        self.laptop_checked = False # Determines if the user has openned Florian's laptop or not
        self.laptop_charged = False # Dertermines if Florian's laptop is charged
        
        
        if not self.laptop_checked:
            print("\nFlorian's laptop sits on the desk, closed.")
            while True:
                choice = input("Do you want to inspect Florian's laptop? (yes/no): ").strip().lower()
                if choice in {"yes", "y"}:
                    print("\nYou open the laptop carefully.")
                    print("The screen is dark. You press the power button...")
                    print("*click*")
                    print("Nothing happens. The battery must be dead.")
                    self.laptop_checked = True
                    
                    if has_charger:
                        print("\n Wait! You have a laptop charger in your inventory!")
                        self._charge_laptop(user_items)
                    else:
                        print("\nYou need a charger to power it on.")
                        print("(Hint: Maybe there's one somewhere in the cellar?)")
                    break
                elif choice in {"no", "n"}:
                    print("You leave the laptop untouched.")
                    break
                else:
                    print("Please answer with yes or no!")
        
        
        elif self.laptop_checked and not self.laptop_charged:
            if has_charger:
                print("\n You have a charger! Maybe you should try it on Florian's laptop?")
                while True:
                    choice = input("Use the charger on the laptop? (yes/no): ").strip().lower()
                    if choice in {"yes", "y"}:
                        self._charge_laptop(user_items)
                        break
                    elif choice in {"no", "n"}:
                        print("You leave the laptop uncharged.")
                        break
                    else:
                        print("Please answer with yes or no!")
            else:
                print("\nThe laptop still needs a charger to turn on.")
        
        
        elif self.laptop_charged:
            print("\nFlorian's laptop is running. The solution code is displayed on the screen.")
            print("You can refer back to it anytime you're in this room.")
        
        return user_items
    
    # Congratulation message when the laptop is being checked wehen fully charged
    
    def _charge_laptop(self, user_items):
        print("\n" + "="*60)
        print("You plug the charger into the wall socket and connect it to the laptop.")
        print("*click*")
        print("A small LED on the laptop lights up - it's charging!")
        print("You press the power button again...")
        print("\n*whirrrr*")
        print("The screen flickers to life!")
        print("="*60)
        print("\nThe laptop boots up. No password required - Florian left it unlocked.")
        print("On the desktop, there's a single file open in a text editor:")
        print("\n" + "─"*60)
        print("PROJECT_SOLUTION.txt")
        print("─"*60)
        print("# ZDD Text Adventure - Final Solution Code")
        print("")
        print("def solve_adventure():")
        print("    steps = [")
        print("        'Explore the ZDD building',")
        print("        'Find items and clues',")
        print("        'Uncover the mystery',")
        print("        'Make meaningful choices'")
        print("    ]")
        print("    return 'Congratulations! You completed the adventure!'")
        print("")
        print("# The real treasure was the friends we made along the way")
        print("# ...and the Python skills we learned!")
        print("─"*60)
        print("\nYou found the Solution Code!")
        print("\nYou take a screenshot with your phone for reference.")
        self.laptop_charged = True
        
       
        user_items[:] = [item for item in user_items if item.name != "laptop charger"]
        
        
        solution = Item(
            "solution code",
            "You have the solution code from Florian's laptop stored on your phone.",
            movable=False
        )
        user_items.append(solution)
# Laptop charger item
laptop_charger = Item(
    "laptop charger",
    "A universal laptop charger with multiple adapter tips. Still warm.",
    movable=True
)


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.", laptop_charger)
gaming_room = GamingRoom('Gaming Room', 'The perfect room to relax and make researches')
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "gaming_room" : gaming_room
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
