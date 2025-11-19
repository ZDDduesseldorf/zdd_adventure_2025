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

class CardioCenter(Room):
    def run_story(self, user_items):
        print("You enter the Cardio Center on the second floor.")
        print("A bright fitness room with a bike, rowing machine, and treadmill.")
        print('A wall display reads: "Challenge available only with wearable!"')
        print()

        has_tracker = "Fitness Tracker" in [x.name for x in user_items]

        if not has_tracker:
            print("You walk toward the display...")
            print("It flashes red: 'No wearable detected. Try again with the proper item.'")
            print("You notice something lying on a towel beside the treadmill.")
            print("It's a Fitness Tracker! Maybe you should pick it up.")
            return user_items

        print("Your Fitness Tracker vibrates.")
        print("The display lights up: 'Start challenge? (yes/no)'")
        choice = input("> ").strip().lower()
        if choice != "yes":
            print("You decide to skip the cardio challenge for now.")
            return user_items

        print("\nYou begin the cardio challenge...")
        print("Bike → Rowing → Treadmill ... your pulse rises.")
        print("'CHALLENGE COMPLETED!' flashes on the display.")

        print("\nA Fitness Card drops out!")
        user_items.append(FitnessCard())
        return user_items

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
cardio_center = CardioCenter(
    "cardio_center",
    "Second floor — Sports and Wellness Area, glass door marked 'Cardio Center'."
)
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "cardio_center": cardio_center
}
