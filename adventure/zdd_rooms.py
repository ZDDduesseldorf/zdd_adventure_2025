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

class GamingLounge(Room):
    def run_story(self, user_items):
        print("Wow, it's a gaming lounge with a huge TV in the corner!")
        # Check if the user has the switch in their inventory; If switch is present start playing a game.
        if "nintendo_switch" in [x.name for x in user_items]:
            user_input = input("You have a switch in your inventory. Do you want to play a game?: (yes/no) ")
            if user_input.lower() == "yes":
                play = True
                # Loop over the game as long as the player answers "yes"
                while play:
                    print("You go to the TV, connect your Nintendo Switch and start playing.")
                    print("This game is super fun! but in the back of your mind, you can’t stop thinking about the portfolio assignment…”)")
                    new_input = input("Do you want to continue playing?: (yes/no) ")
                    if new_input.lower() == "yes":
                        continue
                    elif new_input.lower() == "no":
                        play = False
                    else:
                        print("You're unsure and think again. (Answer 'yes' or 'no')")
                        
            elif user_input.lower() == "no":
                    print("You decide that you don't have time to play right now.")
                    
            else:
                print("You're unsure and think again. (Answer 'yes' or 'no')")

                    
                
        
        

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

gaming_lounge = GamingLounge("Gaming Lounge", "There's a TV but no gaming console...")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gaming_lounge": gaming_lounge
}
