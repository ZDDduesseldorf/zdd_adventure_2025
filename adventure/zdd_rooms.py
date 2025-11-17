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
        "Badminton Book, Der Trick ist: Serve, Slice, Smash, Clear'", 
        "Ein kleines Handbuch", 
        movable=True
        )

        self.golden_shuttlecock = Item(
            "Golden Shuttlecock", 
            "Ein goldener Federball", 
            movable=True
        )

    def enter_room(self, items, command_handler):
        if self.visited == 0:
            print("Du betrittst den Raum:", self.name)
            print(self.description)
            print("Da steht ein Gegner auf einem Feld und starrt dich an.")
        else:
            print("Du bist wieder hier:", self.name)
        self.visited += 1

        while True:
            action = input("> (play match / ask for help / inspect / leave) ").lower()

            if command_handler.handle_global_commands(action):
                if not command_handler.game.game_active:
                    return items
                continue

            if action == "leave":
                print("Du gehst raus.")
                return items

            if action == "inspect":
                print("Eine helle Halle mit einem Badmintonfeld, der Gegner schaut dich böse an")
                if self.enemy_beaten:
                    print("Er sieht jetzt freundlicher aus.")
                elif not self.book_given:
                    print("Vielleicht fragst du ihn um Hilfe (ask for help).")
                continue

            if action == "ask for help":
                if not self.book_given:
                    print("Hmmmpf, lies das.' Du bekommst ein Buch.")
                    items.append(self.badminton_book)
                    self.book_given = True
                else:
                    print("Er sagt: 'Mehr Hilfe kriegst du nicht.'")
                continue

            if action == "play match":
                if self.enemy_beaten:
                    print("Er: 'Schon vorbei. Kein neues Spiel.'")
                    continue
                print("Okay, dann spielen wir ein Match!")
                print("Wie willst du spielen? [Serve/Smash/Clear/Slice]")
                moves = []
                for i in range(4):
                    mv = input(f"Schlag {i+1}: ").lower()
                    moves.append(mv)
                if moves == self.correct_sequence:
                    print("Du gewinnst! Er gibt dir einen goldenen Federball.")
                    items.append(self.golden_shuttlecock)
                    self.enemy_beaten = True
                else:
                    print("Verloren. Falsche Reihenfolge.")
                    if self.book_given:
                        print("Vielleicht noch mal ins Buch schauen.")
                continue

            print("Kenn ich nicht. Versuch was anderes.")

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
badminton_court = BadmintonCourt("Badminton Court", "Ein Raum mit nur einem Badmintonfeld und einem Gegner.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "badminton_court": badminton_court
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
