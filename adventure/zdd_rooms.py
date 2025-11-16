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

class CoffeeKitchen(Room):
    def run_story(self, user_items):
        print("You are in the Coffee kitchen!")
        while True:
         user_action= input("Do you want to do some inspections? If yes, choose an option. a)Coffee machine b)Drawer c)Wall d)Leave ")
         if user_action.lower() == "coffee machine":
            print("Good, the coffee machine seems to be completely broken. Not even a single light is on")
            continue
         elif user_action.lower() == "drawer":
            print("Drawer opened!.")
            if len(self.items) == 0:
               print("Oops empty!")
            else:
             user_action_2=input("OOh, here is a small usb stick. Do you want to take it? (yes/no)")
             if user_action_2.lower()== "yes":
              for item in self.items:
                if item.name.lower()== "mysterious usb stick":
                   user_items.append(item)
                   self.items.remove(item)
                   print("USB Stick picked up!")
             else:
               print("okay.")
            continue
         elif user_action.lower()== "wall":
            print("It seems there is a note on the wall. Ohh, it contains a cryptic clue")
            continue
         elif user_action.lower()== "leave":
            print("Thanks for visiting the Coffee Kitchen")
            break
           
         else:
            print("Choose a right option please...")
            continue
        
        return user_items
    


                   
        
# -----------------------------------------------------------
# ------------------- List here all rooms -------------------
toilet_cellar = ToiletCellar("toilet", "Yes, even the cellar has a toilet.")

# -----------------------------------------------------------
# Add YOUR ROOM instance here, similar to the example below:
coffee_kitchen = CoffeeKitchen("coffee kitchen", "A small, slightly messy coffee kitchen. The main feature is a broken, high-tech coffee machine.")

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
     "coffee kitchen": coffee_kitchen
}
