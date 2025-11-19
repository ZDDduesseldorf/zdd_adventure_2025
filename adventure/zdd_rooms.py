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
class YourRoom(Room):
    def run_story(self, user_items):
        print("You enter your room. It's calm... but something feels off.")

        if "laptop" in [x.name for x in user_items]:
            print("Your laptop suddenly lights up in your backpack.")
            print("A huge wall of unfinished tasks appears on the screen.")
            print("The stress hits you instantly... it's overwhelming.")

            action = input("Do you want to smash the laptop out of frustration? (yes/no): ").strip().lower()

            if action == "yes":
                print("You slam the laptop on the ground. The screen shatters into pieces.")
                print("Strangely enough... you feel a bit better.")
                return [x for x in user_items if x.name != "laptop"]

            print("You hold yourself back and close the laptop.")
            print("You're stressed... but proud of your self-control.")
            return user_items

        else:
            print("You look around. Without your laptop, the room feels strangely quiet.")
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
your_room = YourRoom(
    "your_room",
    "This is your personal space ... you are not alone, work is waiting for you."
)
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")
ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "your_room": your_room,
    "scent_lab": scent_lab
}

