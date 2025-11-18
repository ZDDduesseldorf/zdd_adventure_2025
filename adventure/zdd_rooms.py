"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Room, Item

class FitnessTracker(Item):
    def __init__(self):
        super().__init__(
            name="Fitness Tracker",
            location="cardio_center",
            description=(
                "A smart watch that tracks steps, speed, and pulse. "
                "Its display reads: 'Ready for your next workout?'\n"
                "Lying on a towel beside the treadmill with a note: 'Essential for cardio challenges!'"
            )
        )

class FitnessCard(Item):
    def __init__(self):
        super().__init__(
            name="Fitness Card",
            location="reward",
            description=(
                "A special card awarded for completing the Cardio Room challenge. "
                "It unlocks sports-related areas for future events."
            )
        )

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
        print('A wall display reads: "Challenge available only with wearable!"\n')

        # Prüfen, ob Spieler den Tracker hat
        has_tracker = "Fitness Tracker" in [x.name for x in user_items]

        if not has_tracker:
            print("On a towel beside the treadmill, you see a small device.")
            print("A note beside it reads: 'Essential for cardio challenges!'")
            print("You found a Fitness Tracker! Type 'take tracker' to pick it up.\n")
            print("The wall display flashes red: 'No wearable detected. Try again with the proper item.'")
            return user_items

        # Spieler hat Tracker → Challenge starten
        print("The display detects your Fitness Tracker!")
        print("It lights up: 'Start Challenge? (yes/no)'")
        choice = input("> ").strip().lower()
        if choice != "yes":
            print("You decide to skip the cardio challenge for now.")
            return user_items

        print("\nYou begin the cardio challenge...")
        print("Bike → Rowing Machine → Treadmill ... your pulse rises.")
        print("After an intense workout, the screen flashes: 'CHALLENGE COMPLETED!'")

        print("\nA Fitness Card drops out of a small slot!")
        user_items.append(FitnessCard())

        return user_items

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
    "cardio_center": cardio_center# Add your room key-value pairs here:
    # "my_room_key": my_room
}
