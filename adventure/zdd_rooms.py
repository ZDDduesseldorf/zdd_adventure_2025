"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
from colorama import init, Fore, Back, Style
init()


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

class Cafeteria(Room):
    def run_story(self, user_items):
        print("You enter the cafeteria.")
        print("The room is bright and lively. Long tables, the smell of warm food \n students chatting, and music is playing in the background." + Fore.BLUE)
        
        # checks if the user took the music player 
        has_music_player = any(x.name == "music player" for x in user_items)
        # Speichert, was schon gemacht wurde
        done = {
            "eat": False,
            "listen": False,
            "take": False,
            "use": False
        }

        while True:
            # actions you can do in cafeteria
            print(Fore.RESET + "\nYou can:")
            if not done["eat"]:
                print("- eat food")
            if not done["listen"]:
                print("- listen music")
            if not has_music_player and not done["take"]:
                print("- take music player")
            if has_music_player and not done["use"]:
                print("- use music player")
            print("- leave")

            action = input("\nWhat do you do? ").strip().lower()

            # actions

            if action == "eat food" and not done["eat"]:
                print("You eat a cafeteria pizza. For only 2,50$ crazy deal.")
                done["eat"] = True

            elif action == "listen music" and not done["listen"]:
                print("The music gives you a strangely crippling, unsettling feeling.")
                done["listen"] = True

            elif action == "take music player" and not has_music_player:
                print(Back.RED + "You find a small, old music player on a table and take it." + Back.RESET)
                music_player = Item(
                    "music player",
                    "A small, old portable music player. It still works (most of the time).",
                    movable=True
                )
                user_items.append(music_player)
                has_music_player = True
                done["take"] = True

            elif action == "use music player" and has_music_player and not done["use"]:
                print("You press play.", (Fore.CYAN + "Queen’s 'Bohemian Rhapsody' starts blasting.") + Fore.RESET, (Back.CYAN + "Mamaaaaa Uuuhhh...") + Back.RESET)
                done["use"] = True

            elif action == "leave":
                print("You leave the cafeteria and return to the ground floor.")
                return user_items

            else:
                print("You can't do that right now.")
        # actions you can do in the cafeteria
        """ 
        while True:
            action = input("What do you do in the cafeteria?").strip().lower()

            if action == "eat food":
                print("You grab a plate and eat some pizza. You only paid 2,50$ crazy deal!")
                print("The cafeteria lady was a bit too weird tho.")

            elif action == "listen music":
                print("The music gives you a strangely crippling, unsettling feeling.")

            elif action in {"take music player"}:
                if has_music_player:
                    print("You already took the music player with you. Did you forget?")
                else:
                    print("On a table you find", (Fore.RED + "a small, old portable music player."))
                    print(Fore.RESET + "You don't think twice, you pick it up and put it in your pocket.")
                    music_player = Item(
                        "music player",
                        "A small, old portable music player. It still works, at least most of the time.",
                        movable=True,
                    )
                    user_items.append(music_player)
                    has_music_player = True

            elif action == "use music player":
                if has_music_player:
                    print("You turn on the music player.", (Back.YELLOW + "Queens, Bohemian Rapsody starts playing: MAMMAAAAA UUUHH..." + Back.RESET))
                else:
                    print("You don't have a music player with you. You had to steal it while you had the chance.")

            elif action in {"leave"}:
                print("You leave the cafeteria and step back into the ground floor.")
                return user_items

            else:
                print("Nothing like that to do here.")
                print("Try 'eat food', 'listen music', 'take music player', 'use music player', or 'leave'.")
"""
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
cafeteria = Cafeteria("cafeteria", "A lively cafeteria filled with students and quiet music.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "cafeteria": cafeteria
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
