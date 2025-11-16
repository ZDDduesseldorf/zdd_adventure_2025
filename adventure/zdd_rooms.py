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


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
class BallPitRoom(Room):
    def run_story(self, user_items):
        if self.visited == 1:
            print("You enter the cellar... the entire floor is a giant Ball Pit.")
            print("Colorful plastics balls stretch out like an ocean.")
            print("You feel like this room is meant as a silly little side quest.")
        else:
            print("You step back into the Ball Pit Room. The plastics balls shift around you.")
        return user_items
    
    def enter_room(self, user_items, command_handler):
        self.visited  += 1
        user_items = self.run_story(user_items)

        item_found = False
        while True:
            action = input (">> 'inspect', 'jump in', 'search balls', 'leave': ").strip().lower()

            if command_handler.handle_global_commands(action):
                if not command_handler.game.game_active:
                    return user_items
                continue

            if action == "leave":
                print("You climb out of the Ball Print Room...")
                return user_items
            
            elif action == "jump in":
                print("You take a running start and jump straight into the ball print")

            elif action == "search balls":
                if not item_found:
                    print("You search colorful plastic balls...")
                    print("Something catches your eye")
                    uno = item(
                        "UNO Reverse Card",
                        "A card hidden deep inside the ball pit.",
                        movable = True
                    )
                    self.items.append(uno)
                    print("You found a UNO Reverse Card!")
                    item_found = True
                else:
                    print("You search again, but find nothing new.")

            elif action == "inspect":
                user_items = self.show_items(user_items)

            else:
                print("This room doesn't understand that command. Please try again!")
                
ball_pit_room = BallPitRoom(
    "Ball Pit Room",
    "A room filled with colorful plastic balls."
)

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    "ball_pit": ball_pit_room
}
