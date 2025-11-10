"""This is to keep all special rooms of the ZDD."""
from main_classes import Room ,Item


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


class AiLab(Room):
    def __init__(self, name, description):
        chatbot_item = Item(
            "chatbot terminal",
            "A terminal with a blinking cursor. It seems to be running an old chat program.",
            movable=False
        )
        super().__init__(name, description, chatbot_item)
        self.chatbot_active = False

    def run_story(self, user_items):
        if not any(item.name == "chatbot terminal" for item in self.items):
            print("You already inspected the terminal.")
            return user_items

        print("\nYou approach the 'chatbot terminal'.")
        print("The screen flickers to life as you inspect it.")
        print("CHATBOT: ...Booting... ZDD-DAILIZA v0.2 running...")
        print("CHATBOT: Hello. I am an experimental AI. You can ask me things.")
        print("CHATBOT: (Type 'exit' to stop talking to me)")

        self.chatbot_active = True
        while self.chatbot_active:
            player_input = input("CHATBOT >> ").strip().lower()

            if "hallo" in player_input:
                print("CHATBOT: Hello! I am in the experimentation phase.")
            elif "hilfe" in player_input:
                print("CHATBOT: I can respond to 'hallo'. Type 'exit' to leave.")
            elif "exit" in player_input:
                print("CHATBOT: ...Shutting down conversation module...")
                self.chatbot_active = False
            else:
                print("CHATBOT: My responses are limited. I am still in the experimentation phase.")

        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
ai_lab_room = AiLab("AI Lab", "A room filled with old computers. One of them seems to be running.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "ai_lab": ai_lab_room,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
