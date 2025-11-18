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
    
class SecurityRoom(Room):
    secret_code = "2025"
    def __init__(self, name, description, exits=None):
        super().__init__(name, description, exits)
        self.current_cam = 1
        self.keycard_found = False

    def run_story(self, user_items):
        print("You step into the Security Room. Several monitors glow faintly in the dark.")
        print("The feeds show different parts of the ZDD building.")
        return user_items
    
    def show_items(self, user_items):
        print("You approach the security console and stand in front of the monitor wall.")
        self._print_current_cam()
        saw_code = False
        while True:
            cmd = input(">> Type 'up' or 'down' to switch cameras, or 'back' to stop inspecting: ").strip().lower()

            if cmd in {"up", "down"}:
                self.change_cameras(cmd)
                if self.current_cam == 2:
                    saw_code = True
            elif cmd in {"back", "leave", "exit"}:
                print("You step back from the monitors.")

                if saw_code and not self.keycard_found:
                    self.try_unlock(user_items)
                
                return user_items
            else:
                print("Unknown command. Use 'up', 'down', or 'back'.")

    def change_cameras(self, direction: str):
        if direction == 'up':
            self.current_cam = (self.current_cam % 3) + 1
        elif direction == 'down':
            self.current_cam = ((self.current_cam - 2) % 3) + 1
        
        self._print_current_cam()

    def _print_current_cam(self):
        if self.current_cam == 1:
            print("CAM 1 → A quiet hallway. Nothing unusual.")
        elif self.current_cam == 2:
            print(f"CAM 2 → A whiteboard comes into view. A code is written on it: '{self.secret_code}'.")
        elif self.current_cam == 3:
            print("CAM 3 → Another corridor. Empty and silent.")
    
    def try_unlock(self, user_items):
        print("\nA small console blinks under the monitors. It asks for a 4-digit code.")

        attempt = input("Enter the code: ").strip()
        if attempt == self.secret_code:
            print("The console beeps softly. A hidden compartment slides open.")
            print("Inside you find a keycard.")
            user_items.append(keycard)
            self.keycard_found = True
        else:
            print ("The console flashes red. Incorrect code.")
        return user_items


keycard = Item("keycard", "A magnetic card granting access to restricted areas.", movable=True)
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
securityroom_first = SecurityRoom("security room", "This is the total secret room")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "securityroom_first": securityroom_first
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
