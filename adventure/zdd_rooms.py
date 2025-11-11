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

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

class Balcony(Room):
    def __init__(self, name, description, items_init=None):
        super().__init__(name, description, items_init)
        self.quiz_solved = False  # Eigener Status für den Raum

    def run_story(self, user_items):
        # Zeige die Raumbeschreibung
        if self.visited == 1:
            print("You step out onto a windy balcony on the top floor.")
            print("In the corner, you see a metal suitcase with a 3-digit combination lock.")
        else:
            print("You are back on the balcony.")

        # Prüfen, ob das Rätsel schon gelöst ist
        if self.quiz_solved:
            print("The suitcase is already open.")
            return user_items # Nichts mehr zu tun hier
        
        # Rätsel-Logik aus Issue #13 (Mathe-Quiz)
        print("\nThe lock on the suitcase shows a math problem: 7 * (7 - 4)")
        action = input("Try to enter the 3-digit code: ")

        if action.strip() == "021": # Die richtige Antwort (7 * 3 = 21)
            print("\n*CLICK!* The lock springs open!")
            print("Inside the suitcase, you find a... FLASHLIGHT!")
            
            # Belohnung (Item) zum Raum hinzufügen
            flashlight = Item("Flashlight", "A sturdy flashlight. It seems to work.", movable=True)
            self.items.append(flashlight) # Item erscheint jetzt im Raum
            self.quiz_solved = True       # Rätsel als gelöst markieren
        else:
            print("\n*BEEP!* Wrong code. The lock remains shut.")

        return user_items

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
balcony = Balcony("balcony", "A windy balcony on the top floor.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "balcony": balcony
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
