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
        while True:
            cmd = input(">> Type 'up' or 'down' to switch cameras, or 'back' to stop inspecting: ").strip().lower()

            if cmd in {"up", "down"}:
                self.change_cameras(cmd)
            elif cmd in {"back", "leave", "exit"}:
                print("You step back from the monitors.")
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



class Scentlab(Room):
    def run_story(self, user_items):
        if self.visited == 1:
            print("You walk into the Scentlab...What an interesting room, you think to yourself.")
            print("Suddenly, a diffuser sprays a mysterious scent into the room!")
            print("As the mist settles, you notice a shimmering pink perfume bottle on the floor.")

            perfume = Item(
                name="experimental perfume bottle",
                description="A shimmering pink perfume bottle. The scent keeps shifting.",
                movable=True
            )
            self.items.append(perfume)

        else:
            print()
        return user_items
    
    def enter_room(self, user_items, command_handler):
        self.visited += 1
        print("You step into the Scentlab.")
        user_items = self.run_story(user_items)

        while True:
            action = input(">> smell perfumes / inspect shelves / inspect perfume / leave: ").strip().lower()
            if command_handler.handle_global_commands(action):
                return user_items
            if action == "leave":
                print("You leave the Scentlab.")
                return user_items
            elif action == "smell perfumes":
                print("You smell different fragrances...floral, sweet, and something strangely metallic.")
            elif action == "inspect shelves":
                print("The shelves are full of labelled and unlabbeled bottles. Some even glow softly.")
            elif action == "inspect perfume":
                if not self.items:
                    print("There is no perfume bottle here anymore.")
                else:
                    for item in self.items:
                        print(item.description)
                        if item.movable:
                            take = input(">> Do you want to take the perfume bottle? (yes/no): ").strip().lower()
                            if take == "yes": 
                                user_items.append(item)
                                self.items.remove(item)
                                print("You took the perfume bottle.")
                            else:
                                print("You decided to leave the perfume bottle.")
            else: 
                print("Unknown Command.")
            
        
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
securityroom_first = SecurityRoom("security room", "This the total secret room")
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "securityroom_first": securityroom_first,
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "scent_lab": scent_lab

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "scent_lab": scent_lab
}
