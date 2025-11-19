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

class OfficeHulinski(Room):
    def run_story(self, user_items):
        print("You enter Hulinski's office, filled with books and papers that seem to be exams.")
        print("The semmingly annoyed Hulinski sits behind his desk and mubles: 'Where is that darn red pen! Without it, I cannot faile these idi- i mean beloved students.' .")
        return user_items
    
    def enter_room(self, user_items, command_handler):
        self.visited += 1
        user_items = self.run_story(user_items)

        while True:
            action = input(">> talk to Hulinski / inspect desk / leave: ").strip().lower()
            if command_handler.handle_global_commands(action):
                return user_items
            if action == "leave":
                print("You leave Hulinski's office.")
                return user_items
            elif action == "talk to Hulinski":
                print("Do you have my red pen? I can't grade without it!")
                if "red pen" in user_items:
                    print("Oh, you have it! Thank you so much! ... this is your best friend? Damn ... I will nonetheless fail him .")
                else:
                    print("Du hast keinen roten Stift.")
            elif action == "inspect desk":
                print("You see the exam of zour best friend and know he is cooked.")
            else:
                print("Unknown Command.")
            
        
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "scent_lab": scent_lab
}
