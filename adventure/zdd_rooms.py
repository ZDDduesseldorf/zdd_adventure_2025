"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item


# -----------------------------------------------------------
# ---------------------- Toilet Cellar -----------------------
# -----------------------------------------------------------

class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print("While you wash your hands, the book slips out of your backpack ...right into the water.")
            print("You decide that it wasn't that important after all.")
            return [x for x in user_items if x.name != "old book"]
        return user_items


# -----------------------------------------------------------
# ----------------------- Scent Lab --------------------------
# -----------------------------------------------------------

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

        return user_items


# -----------------------------------------------------------
# --------------------- New Room: Terrace --------------------
# -----------------------------------------------------------

class Terrace(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.first_visit = True

    def run_story(self, user_items):
        if self.first_visit:
            print("\nYou step through the door at the end of the corridor and onto the roof terrace above the ZDD building.")
            print("A cold wind hits your face. The city lights of Düsseldorf stretch beneath you.")
            print("It feels slightly unsafe, as if students aren’t really supposed to be here.")
            print("You take a deep breath. Wow.")
            self.first_visit = False
        else:
            print("\nYou are back on the cold rooftop terrace. The city lights shimmer below.")

        while True:
            command = input("\nWhat do you do? (inspect / look / leave): ").strip().lower()

            if command in ["inspect", "look"]:
                print("The rooftop offers a wide open view of Düsseldorf. The wind is sharp and the city hums quietly below.")

            elif command == "leave":
                print("You step back inside to the third floor corridor.")
                break

            else:
                print("Unknown command. Try: inspect / look / leave.")

        return user_items


# -----------------------------------------------------------
# ---------------------- Create Rooms ------------------------
# -----------------------------------------------------------

toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")
terrace = Terrace("terrace", "A rooftop terrace above the ZDD building with a cold night view over Düsseldorf.")


# -----------------------------------------------------------
# ---------------------- ALL ROOMS LIST ----------------------
# -----------------------------------------------------------

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "scent_lab": scent_lab,
    "terrace": terrace,
}