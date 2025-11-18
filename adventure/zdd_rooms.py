"""This is to keep all special rooms of the ZDD."""
from main_classes import Room, Item
import random


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

class HiddenVRLab(Room):
    def run_story(self, user_items):
        print("You step into a dimly lit, futuristic room filled with cables and glowing LEDs.")
        print("A broken VR headset lies on a metal table, and a giant curved screen on the back wall flickers to life.")
        print("-" * 40)
        
        print("The screen displays a rapid sequence of numbers and then settles on three:")
        
        random_numbers = []
        for i in range(3):
            new_number = random.randint(1, 100)
            random_numbers.append(new_number)

        num1 = random_numbers[0]
        num2 = random_numbers[1]
        num3 = random_numbers[2]

        print(f"[{num1}] ... [{num2}] ... [{num3}]")
        
        prediction = ""
        while prediction not in ["higher", "lower"]:
            prediction = input("A prompt appears: 'Will the next number be HIGHER or LOWER than the last one?' >> ").strip().lower()

        next_number = random.randint(1, 100)
        print(f"The next number is... [{next_number}]!")

        if next_number > num3:
            actual_result = "higher"
        else:
            actual_result = "lower"
        
        if prediction == actual_result:
            print(">> Simulation success. Your instincts are sharp!")
        else:
            print(">> Simulation crashed… as expected.")
            
        return user_items


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
vr_lab_room = HiddenVRLab("Hidden VR-Lab", "An experimental and slightly chaotic prototype lab.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "vr_lab": vr_lab_room
}
