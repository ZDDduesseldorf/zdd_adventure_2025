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

# Issue #97 Roof Terrace ---
class RoofTerrace(Room):
    def run_story(self, user_items):
        print("A cold wind hits your face.")
        print("You can see the lights of Düsseldorf shimmering in the distance.")
        print("It feels a bit lonely up here, but the view is amazing.")
        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# Instanz für die Terrasse erstellen
roof_terrace = RoofTerrace("terrace", "An open roof terrace with a view over the city at night.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "terrace": roof_terrace  # 
}