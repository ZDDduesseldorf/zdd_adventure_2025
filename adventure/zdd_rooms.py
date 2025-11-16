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
        print("You are in the Coffee kitchen!")  #appears each time you enter
        while True:  #This loop will enable actions to be carried out in teh coffee kitchen
         user_action= input("Do you want to do some inspections? If yes, choose an option. a)Coffee machine b)Drawer c)Wall d)Leave ")
         if user_action.lower() == "coffee machine":
            print("Good, the coffee machine seems to be completely broken. Not even a single light is on")
            continue
         elif user_action.lower() == "drawer":  #inspect drawer
            print("Drawer opened!.")
            if len(self.items) == 0:         #counts the number of items in the coffee kitchen. if==0 means drawer is also empty
               print("Oops empty!")
            else:
             user_action_2=input("OOh, here is a small usb stick. Do you want to take it? (yes/no)")
             if user_action_2.lower()== "yes":
              for item in self.items:
                if item.name.lower()== "mysterious usb stick":     #if the name of item in drawer== ...
                   user_items.append(item)                         #Add in inventory list
                   self.items.remove(item)                         #delete from coffee kitchen
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
#New item in Coffe kitchen
usb_stick= Item("mysterious usb stick", "Its purpose is to be used in another location. For example, if the player has the Mysterious USB Stick in their inventory, they can use stick or inspect computer in the AI Lab to unlock a new clue, solve a puzzle, or gain access to a new area",True) 
coffee_kitchen = CoffeeKitchen("coffee kitchen", "A small, slightly messy coffee kitchen. The main feature is a broken, high-tech coffee machine.", items_init=[usb_stick])

ALL_ROOMS = {
    "toilet_cellar": toilet_cellar,
     "coffee kitchen": coffee_kitchen
}
