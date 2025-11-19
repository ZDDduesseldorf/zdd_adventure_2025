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
            
class RubiksCube2x2:
    def __init__(self):
        # Farben: W=up, R=right, G=front, Y=down, O=left, B=back
        self.cube = [
            'W','W','W','W',   # Up
            'R','R','R','R',   # Right
            'G','G','G','G',   # Front
            'Y','Y','Y','Y',   # Down
            'O','O','O','O',   # Left
            'B','B','B','B'    # Back
        ]

    def is_solved(self):
        # Prüfe, ob jeder Face 4 gleiche Farben hat
        for i in range(0, 24, 4):
            if len(set(self.cube[i:i+4])) > 1:
                return False
        return True

    def rotate_U(self):
        self._cycle([0,1,3,2])
        self._cycle([8,9,20,21,4,5,16,17])

    def rotate_R(self):
        self._cycle([4,5,7,6])
        self._cycle([1,3,18,20,13,15,9,11])

    def rotate_F(self):
        self._cycle([8,9,11,10])
        self._cycle([2,3,16,18,13,12,7,6])

    def rotate_L(self):
        self._cycle([16,17,19,18])
        self._cycle([0,2,12,14,10,8,21,23])

    def rotate_D(self):
        self._cycle([12,13,15,14])
        self._cycle([10,11,5,7,22,23,1,0])

    def rotate_B(self):
        self._cycle([20,21,23,22])
        self._cycle([0,1,6,4,13,12,19,17])

    def _cycle(self, positions):
        vals = [self.cube[pos] for pos in positions]
        for i, pos in enumerate(positions):
            self.cube[pos] = vals[i-1]

    def scramble(self, turns=10):
        import random
        moves = [self.rotate_U, self.rotate_R, self.rotate_F, self.rotate_L, self.rotate_D, self.rotate_B]
        for _ in range(turns):
            random.choice(moves)()

    def print_cube(self):
        faces = ['Up', 'Right', 'Front', 'Down', 'Left', 'Back']
        for i, face in enumerate(faces):
            print(f"{face}: {self.cube[i*4:(i+1)*4]}")

def play():
    cube = RubiksCube2x2()
    cube.scramble()
    print("You enter the Silent Puzzle Room. Silence surrounds you. In front of you is a 24-faced Rubik’s Cube.")
    while True:
        cube.print_cube()
        if cube.is_solved():
            print("Congratulations! You solved the silent cube! You gain a small reward (key fragment).")
            break
        move = input("Enter move (U, R, F, L, D, B) or 'quit': ").upper()
        if move == 'QUIT':
            print("You abandon the puzzle, leaving it unsolved.")
            break
        elif move == 'U':
            cube.rotate_U()
            print("Performed U move.")
        elif move == 'R':
            cube.rotate_R()
            print("Performed R move.")
        elif move == 'F':
            cube.rotate_F()
            print("Performed F move.")
        elif move == 'L':
            cube.rotate_L()
            print("Performed L move.")
        elif move == 'D':
            cube.rotate_D()
            print("Performed D move.")
        elif move == 'B':
            cube.rotate_B()
            print("Performed B move.")
        else:
            print("Invalid move. Please enter U, R, F, L, D, B or quit.")

if __name__ == "__main__":
    play()

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
scent_lab = Scentlab("Scent Lab", "A small lab filled with glowing perfume bottles and mysterious scents.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "scent_lab": scent_lab
}
