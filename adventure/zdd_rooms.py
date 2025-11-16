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

class ServerRoom(Room):
    def run_story(self, user_items):
        system_patch_usb = Item("System Patch USB", "A simpl USB stick labeled SYSTEM_PATCH_V3. It looks official", movable=True) # Iniitialize the Seystem Patch USB
        self.power_is_on = True # Set Power On initially
        print("You enter the room, the server make loud noises and the light is on.") # Story introduction
        print("You see a console with the 'Main Server Terminal' and a large red 'Main Power Switch' on the wall.") # Story introduction
        user_inp = input("Do you want to pick up the 'System Patch USB' from the console? (yes/no):\n>") # Ask if item should be picked up
        if user_inp.lower() == 'yes': # If yes, add to inventory
            print("You picked up the 'System Patch USB' and put it in your backpack.")
            user_items.append(system_patch_usb)
        else: # If no, do nothing
            print("You chose not to pick up the 'System Patch USB'.")
        user_inp = input("What do you want to do? A for inspect and B for flippung the switch:\n>") # Ask for next action
        if user_inp.lower() == 'a': # If inspect
            print("The terminal shows: > ERROR! Security protocols active. Please initiate maintenance mode.") 
            print("The switch is in the 'ON' position.")
            user_inp = input("Do you want to flipp the 'Main Power Switch'now? (yes/no):\n>") # Ask if switch should be flipped
            if user_inp.lower() == 'yes': # If yes, turn off power
                print("You pull the large switch. The whir of the servers dies. The room is now quiet, and the 'Main Server Terminal' screen flickers to a 'MAINTENANCE MODE' prompt.")
                self.power_is_on = False
            else: # If no, do nothing
                print("You chose not to flipp the switch. The servers remain online. And since nothing happens you leave")
                return user_items # Exit because of no action
        elif user_inp.lower() == 'b': # If flip switch directly
            print("You pull the large switch. The whir of the servers dies. The room is now quiet, and the 'Main Server Terminal' screen flickers to a 'MAINTENANCE MODE' prompt.")
            self.power_is_on = False # Set power off
        if "System Patch USB" in [x.name for x in user_items]: # Check if user has the USB
            user_inp = input("Do you want to insert the 'System Patch USB' into the terminal? (yes/no):\n>") # Ask if USB should be inserted
            if user_inp.lower() == 'yes': # If yes, run patching story
                print("TERMINAL: > Maintenance Mode Active. You insert the 'System Patch USB'. > PATCH APPLIED... .A log file opens, revealing a hidden message: To: Prof. Huber -- We have to stop using the cellar archive as a dead drop. Its too risky. Im moving the prototype key to the roof lab as soon as the power is stable. Dont tell Julian.")
                print("You can reactivate the power now!")
            else: # If no, do nothing
                print("You should insert the System Patch USB to fix the system.")
                print("You failed to fix the system.")
                return user_items # Exit because of no action
            user_inp = input("Do you want to reactivate the power by flippung the 'Main Power Switch' back on? (yes/no):\n>") # Ask if power should be reactivated
            if user_inp.lower() == 'yes': # If yes, turn power on
                print("You flip the switch back. The servers comes back to life. Thank you!")
                self.power_is_on = True
                return user_items # Exit after successful action
            else:
                print("You chose not to reactivate the power. The servers remain offline.")
                return user_items # Exit because of no action
        else:
            print("You don't have the 'System Patch USB' to fix the system.")
            print("You failed to fix the system.")
            return user_items # Exit because of missing item
            

        
    

        

# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")

server_room = ServerRoom("Server Room", "A loud room filled with server racks. A 'Main Server Terminal' sits on a console, and a large red 'Main Power Switch' is on the wall.") # Instance of Server Room

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
    "server_room": server_room # Addition of Server Room instance
}
