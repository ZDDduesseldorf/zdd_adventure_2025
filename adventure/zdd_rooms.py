"""This is to keep all special rooms of the ZDD."""
from main_classes import Room
from main_classes import Item


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

class Labyrinth(Room):
    def run_story(self, user_items):
        print("You enter a room that looks like a labyrinth.")
        choice = input("Do you want to go through it? (yes/no): ").strip().lower()

        if choice == "no":
            print("You avoid the labyrinth and stay safe.")
            return user_items

        import random
        outcome = random.choice(["treasure", "lost"])

        if outcome == "treasure":
            print("You found a treasure! +20 bonus points for the stochastic exam!")
        
        # EKI
 #           print("You also find a sheet of paper with EKI math equations on it.")
            
 #           self.items.append(
  #              Item("EKI paper", 
   #                 "A sheet full of EKI math equations. Might help with the EKI exam.",
    #                movable=True)
     #       )

        else:
            print("You got lost and arrive late for the DSAI final presentation.")

        print("There might be something lying around here...")

        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
labyrinth = Labyrinth(
    "labyrinth", 
    "A confusing maze with uncertain outcomes.",
    items_init=[Item("EKI paper",
                    "A sheet full of EKI math equtions. Might help with the EKI exam.",
                    movable=True)]
    )
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "labyrinth": labyrinth,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
