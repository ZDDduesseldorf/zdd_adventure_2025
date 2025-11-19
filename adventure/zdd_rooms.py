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

from main_classes import Room, Item

class SecretRoom(Room):
    def run_story(self, user_items):
        print("You've entered the secret room.")  
        print("In front of you are three drawers: A, B and C.")
        print("One of the drawers may contain something useful...")
        # Player can choose multiple times until they find the pen or leave
        while True:
            choice = input("Which drawer do you want to open? (A/B/C): ").strip().lower()
            if choice == "b":
                print("You open drawer B and find an invisible ink pen!")
                pen = Item("invisible ink pen", "A pen that can reveal secret messages.")
                user_items.append(pen)
                print("You take the pen and notice a nearby note...")
                print("At first, the note seems blank.")
                # Player decides whether to use the pen or not
                reveal_choice = input("Do you want to use the pen and see the message? (yes/y to reveal): ").strip().lower()
                if reveal_choice in ["yes", "y"]:
                   print("The pen glows and the hidden message appears:")
                   print(" 'Soon you are going to be trapped in a room!'")
                else:
                   # Player chooses not to reveal the message
                   print("You leave the note blank. Maybe you weren't the chosen one.")
                break

            elif choice in ["a", "c"]:
                 print(f"Drawer {choice.upper()} is empty. Maybe try a different one.")

            elif choice in ["leave"]:
                    # Player decides to leave the drawers alone
                    print("You decide to leave the drawers alone.")
                    break
            else:
                print("Invalid choice. Please choose A, B, C, or type 'leave' to exit.")
        return user_items
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
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")

secret_room = SecretRoom("secret_room", "A hidden room with mysterious drawers.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "secret_room": secret_room 
    "scent_lab": scent_lab
}
