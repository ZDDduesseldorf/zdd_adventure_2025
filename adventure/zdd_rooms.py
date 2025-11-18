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


# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
# my_room = MyRoom("room_name", "room_description")
class EndlessRoom(Room):
    def run_story(self, user_items):
        self.visited += 1 
        
        
        if self.visited <= 1:
            print(f"You've entered the {self.name}.")
            print("When you take your first steps, you realize you are back at the entrance.")
            print("It feels like you are walking in a circle, but the path is straight.")
            self.description = "The room seems normal, but every step leads back to the start."
            
        
        elif self.visited < 3:
            print("You try again, walking the straight line, but you inevitably end up back at the start. The cycle repeats.")
            
        
        elif self.visited == 3:
            print("You hear a **metallic sound**. Frustrated, you look down and find a strange key lying on the ground!")
            
            
            if self.items == []:
                 self.items.append(chameleon_key)
            
        else:
            print("The endless cycle continues. Maybe the key can change something?")

        return user_items


endless_room = EndlessRoom(
    name="endless room", 
    description="The air is still, and you feel a strange pull towards the entrance."
)
ALL_ROOMS = {
    "toilet_cellar": toilet_cellar
    # Add your room key-value pairs here:
    # "my_room_key": my_room
    "endless_room_key": endless_room
    
}
