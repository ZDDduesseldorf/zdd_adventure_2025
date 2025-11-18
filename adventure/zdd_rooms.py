"""This is to keep all special rooms of the ZDD."""
from main_classes import Item, Room


class ToiletCellar(Room):
    def run_story(self, user_items):
        print("What did you expect? It's a toilet.")
        if "old book" in [x.name for x in user_items]:
            print(
                "While you wash your hands, the book slips out of your backpack "
                "...right into the water."
            )
            print("You decide that it wasn't that important after all.")
            return [x for x in user_items if x.name != "old book"]
        return user_items


# -----------------------------------------------------------
# ------------------- New item: Laptop ----------------------
# -----------------------------------------------------------

laptop = Item(
    name="laptop",
    description=(
        "A laptop sitting on the table, used to build the ZDDAdventure project. "
        "Interacting with the laptop shows the homework you are supposed to do "
        "for the ZDDAdventure project."
    ),
    movable=False,
)

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
# -----------------------------------------------------------

toilet_cellar = ToiletCellar(
    "toilet",
    "Yes, even the cellar has a toilet.",
    items_init=[laptop],
)

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar
}