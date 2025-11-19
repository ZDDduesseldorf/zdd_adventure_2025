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


class GamingLounge(Room):
    def run_story(self, user_items):
        print("Wow, it's a gaming lounge with a huge TV in the corner!")
        # Check if the user has the switch in their inventory; If switch is present start playing a game.
        if "Nintendo Switch" in [x.name for x in user_items]:
            user_input = input("You have a switch in your inventory. Do you want to play a game?: (y/n) ")
            if user_input.lower() == "y":
                play = True
                # Loop over the game as long as the player answers "y"
                while play:
                    print("You go to the TV, connect your Nintendo Switch and start playing.")
                    print("This game is super fun! but in the back of your mind, you can’t stop thinking about the portfolio assignment…”)")
                    new_input = input("Do you want to continue playing?: (y/n) ")
                    if new_input.lower() == "y":
                        continue
                    elif new_input.lower() == "n":
                        play = False
                    else:
                        print("You're unsure and think again. (Answer 'y' or 'n')")
                        
            elif user_input.lower() == "n":
                    print("You decide that you don't have time to play right now.")
                    
            else:
                print("You're unsure and think again. (Answer 'y' or 'n')")
        return user_items

                    
                
        
        
=======
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

gaming_lounge = GamingLounge("Gaming Lounge", "There's a TV but no gaming console...")
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "gaming_lounge": gaming_lounge
    "scent_lab": scent_lab
}
