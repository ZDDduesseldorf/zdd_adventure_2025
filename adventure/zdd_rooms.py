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


class BreakroomFirstFloor(Room):
    gold_coin = Item("coin", "It seems quite valuable. Maybe you can spend it for something useful.", movable=True)
    
    #input invalid
    def invalid(self):
        print("Not a valid interaction")

    def run_story(self, user_items):
        #progress counter
        prog_counter = 0
        
        
        print("You enter a small, but cozy breakroom.")
        print("On the left are two plastic chairs at a woodentable.")
        print("On the rigth is a comfy couch")
        print("Right next to the couch is a large vending machine with snacks and drinks")

        while True:
            if prog_counter == 0:
                action = input("What would you like to do? Go to (table/couch/vending machine/leave room): ").strip().lower()

                #leaving room
                if action in {"leave room"}:
                    return user_items
                
                #invalid input
                if action not in {"table", "couch", "vending machine"}:
                    self.invalid()
                    continue
                else:
                    prog_counter = 1
                    continue
            
            if prog_counter == 1:
                #interaction at the table
                if action in {"table"}:
                    action = input("You're at the table. what next? Inspect (right chair/left chair/table): ").strip().lower()
                    if action not in {"right chair", "left chair", "table"}:
                        self.invalid()
                        action = "table"
                        continue

                    #right chair interaction
                    if action in {"right chair"}:
                        print("On the chair is a engraving. It says: '2+2=4'}.")
                        action = "table"
                        continue

                    #left chair interaction
                    if action in {"left chair"}:
                        print("There is nothing noticeable}.")
                        action = "table"
                        continue

                    #interaction with table
                    if action in {"table"} and self.gold_coin not in user_items:
                        print("Under the table you find a small box with a simple 3-digit combination lock.")
                        action = input("You may enter a combination. (enter 3 digits or input 'leave' to back off): " ).replace(" ","").lower()
                        #interaaction with box
                        if action in {"leave"}:
                            action = "table"
                            continue
                        if action in {"224"}:
                            print("The box opens!")
                            print("You gain two *Coins*!")
                            user_items.append(self.gold_coin)
                            prog_counter = 0
                            print("You go back to the entrance of the room.")
                            action = "table"
                            continue
                        else:
                            print("Nothing happens... Better watch out for any hints.")
                            prog_counter = 0
                            continue
                    if action in {"table"}:
                        print("There is nothing undiscovered under the table.")
                        print("You go back to the entrance of the room.")
                        prog_counter = 0
                        continue
                
                #couch interaction
                if action in {"couch"}:
                    action = input("You're standing in front of the couch. (sit/leave): ").strip().lower()
                    if action in {"sit"}:
                        print("Now you sit... Quite relaxing")
                        print("Better get up!")
                        print("You go back to the entrance of the room.")
                        prog_counter = 0
                        continue
                    if  action in {"leave"}:
                        print("You go back to the entrance of the room.")
                        prog_counter = 0
                        continue
                    else:
                        self.invalid()
                        action = "couch"
                        continue
                
                #interaction with vending machine
                if action in {"vending machine"}:
                    print("The vending machine has only one item, an energy drink.")
                    if self.gold_coin in user_items:
                        action = input("You could use the gold coin to buy the drink. (yes/no): ")
                        if action in {"yes"}:
                            print("You insert the coin... Nothing happens")
                            print("Well, that's a bummer.")
                            print("You leave the room empty handed.")
                            return user_items
                        if action in {"no"}:
                            print("Well, then better go and do something productive")
                            return [x for x in user_items if x.name != "old book"]
                        else:
                            self.invalid()
                            action = "vending machine"
                            continue
                    else:
                        print("You have no money. Maybe go and earn some.")
                        print("You go back to the entrance of the room.")
                        prog_counter = 0
                        continue
            return user_items



# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")
Breakroom_first_floor = BreakroomFirstFloor("Breakromm", "Take a little break.")
# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")



ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "Breakroom": Breakroom_first_floor 
    # Add your room key-value pairs here:
    # "my_room_key": my_room
}
