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
    

class QuickThinkingRoom(Room):
    def run_story(self, user_items):
        print("You enter a modern classroom on the first floor.")
        print("A digital screen lights up with a quick-thinking challenge.\n")

        # Player chooses a number
        number_str = input("Choose any whole number: ")

        if not number_str.isdigit():
            print("That's not a valid number. The challenge shuts down.")
            return user_items

        number = int(number_str)

        print("\nGreat. Your task:")
        print("1) Multiply your number by 2")
        print("2) Add 5")
        print("3) Subtract 3\n")

        correct_solution = (number * 2) + 5 - 3

        answer_str = input("What is the final result? ")

        if not answer_str.isdigit():
            print("That doesn't look like a number. The screen turns off.")
            return user_items

        answer = int(answer_str)

        if answer == correct_solution:
            print("\nCorrect! You solved the challenge.")
            print("A small compartment opens (it's empty for now).")
        else:
            print(f"\nWrong! The correct answer was {correct_solution}.")
            print("The screen fades out.")

        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
# List here all rooms
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
quick_thinking_room = QuickThinkingRoom(
    "Quick Thinking Challenge Room",
    "A first-floor room where students solve quick-thinking challenges."
)

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "quick_thinking_room": quick_thinking_room,
}