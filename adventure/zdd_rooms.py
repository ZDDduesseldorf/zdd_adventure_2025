"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
from main_classes import CommandHandler



class BadmintonCourt(Room):

    def __init__(self, name, description):
        Room.__init__(self, name, description, items_init=None)
        self.enemy_beaten = False
        self.book_given = False
        self.correct_sequence = ["serve", "slice", "smash", "clear"]

        self.badminton_book = Item(
        "Badminton Book: The trick is: Serve, Slice, Smash, Clear", 
        "A small handbook", 
        movable=True
        )

        self.golden_shuttlecock = Item(
            "Golden Shuttlecock", 
            "A golden shuttlecock", 
            movable=True
        )

    def enter_room(self, items, command_handler):
        if self.visited == 0:
            print("You enter the room:", self.name)
            print(self.description)
            print("There is an opponent on the court staring at you.")
        else:
            print("You are here again:", self.name)
        self.visited += 1

        while True:
            action = input("> (play match / ask for help / inspect / leave) ").lower()

            if command_handler.handle_global_commands(action):
                if not command_handler.game.game_active:
                    return items
                continue

            if action == "leave":
                print("You leave.")
                return items

            if action == "inspect":
                print("A bright hall with a badminton court; the opponent glares at you.")
                if self.enemy_beaten:
                    print("He looks friendlier now.")
                elif not self.book_given:
                    print("Maybe ask him for help (ask for help).")
                continue

            if action == "ask for help":
                if not self.book_given:
                    print("Hmmmpf, read this. You receive a book.")
                    items.append(self.badminton_book)
                    self.book_given = True
                else:
                    print("He says: 'You won't get any more help.'")
                continue

            if action == "play match":
                if self.enemy_beaten:
                    print("He says: 'It's already over. No new game.'")
                    continue
                print("Okay, then we'll play a match!")
                print("How will you play? [Serve/Smash/Clear/Slice]")
                moves = []
                for i in range(4):
                    mv = input(f"Schlag {i+1}: ").lower()
                    moves.append(mv)
                if moves == self.correct_sequence:
                    print("You win! He gives you a golden shuttlecock.")
                    items.append(self.golden_shuttlecock)
                    self.enemy_beaten = True
                else:
                    print("Lost. Wrong sequence.")
                    if self.book_given:
                        print("Maybe take another look in the book.")
                continue

            print("I don't know that. Try something else.")

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


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
badminton_court = BadmintonCourt("Badminton Court", "A room with only a badminton court and an opponent.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "badminton_court": badminton_court
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
