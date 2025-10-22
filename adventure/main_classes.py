"""
ZDD Text Adventure Game Framework.

This module provides the basic structure for a text-based adventure game,
including classes for handling commands, representing game items, rooms, and floors.
The framework allows for building interactive environments where players can explore rooms,
collect items, and navigate between floors.

Classes:
    - CommandHandler: Manages global commands like 'exit' and 'inventory'.
    - Item: Represents individual game items with properties and interactions.
    - Room: Encapsulates game rooms with descriptions, items, and interactions.
    - Floor: Organizes rooms and their interconnections on a specific level of the game environment.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Protocol
import textwrap

# ----------------------------- UI helper ----------------------------- #
class UI:
    """
    Small helper for consistent, lightweight console rendering.

    Provides simple building blocks (titles, panels, bullet lists, dividers)
    to make the text adventure easier to read without external libraries.
    Adjust `WIDTH` if your terminal wraps too early or too late.
    """
    WIDTH = 78

    @staticmethod
    def divider(char: str = "─") -> str:
        return char * UI.WIDTH

    @staticmethod
    def title(text: str) -> str:
        text = f" {text} "
        side = max(0, (UI.WIDTH - len(text)) // 2)
        return f"{'=' * side}{text}{'=' * (UI.WIDTH - side - len(text))}"

    @staticmethod
    def subtitle(text: str) -> str:
        return f"• {text}"

    @staticmethod
    def panel(title: str, body: str) -> str:
        lines = [f"[ {title} ]", UI.divider("─")]
        wrapped = textwrap.fill(body, width=UI.WIDTH)
        lines.append(wrapped)
        return "\n".join(lines)

    @staticmethod
    def bullets(items: List[str], indent: int = 2) -> str:
        pad = " " * indent
        return "\n".join(f"{pad}• {s}" for s in items)

    @staticmethod
    def hint(text: str) -> str:
        return f"{textwrap.fill('(hint) ' + text, width=UI.WIDTH)}"

# ----------------------------- Protocol ----------------------------- #
class ZDDAdventureLike(Protocol):
    items: List["Item"]
    game_active: bool

# ----------------------------- Core classes ----------------------------- #
class CommandHandler:
    """Handles global commands like 'exit' and 'inventory'."""

    def __init__(self, game: ZDDAdventureLike):
        self.game = game

    def handle_global_commands(self, command: str) -> bool:
        cmd = command.strip().lower()
        if cmd == "exit":
            print("Thank you for exploring the ZDD!")
            self.game.game_active = False
            return True
        if cmd == "inventory":
            print(UI.title("INVENTORY"))
            if len(self.game.items) == 0:
                print("Your pockets are empty... as well as your hands... sad.")
            else:
                names = [x.name.upper() for x in self.game.items]
                print(UI.bullets(names))
            print(UI.divider())
            return True
        if cmd in {"help", "?"}:
            print(UI.title("HELP"))
            print(UI.bullets([
                "Global: inventory, help, exit",
                "Navigate floors: go <direction>  (e.g., go up / go down)",
                "Enter rooms:   enter <room-label> (e.g., enter archive)",
                "Inside rooms:  inspect / look / leave",
            ]))
            print(UI.divider())
            return True
        return False


@dataclass
class Item:
    """
    Represents an object that can exist in a room or in the player's inventory.

    Items are the main way to model game state and interactions. Some items are
    **movable** and can be picked up by the player; others are purely decorative
    or too heavy to carry.

    Parameters
    ----------
    name : str
        The display name of the item (e.g., "old book").
    description : str
        A short text describing what the player sees when inspecting the item.
    movable : bool, default False
        If True, the item can be added to the player's inventory.

    Attributes
    ----------
    name : str
        The display name of the item.
    description : str
        Descriptive text shown when the item is listed or inspected.
    movable : bool
        Whether the player may pick up the item.
    """

    name: str
    description: str
    movable: bool = False

    def describe(self) -> None:
        """Print the item's description to the console."""
        print(self.description)

    def is_movable(
        self,
        user_items: List["Item"],
        other_item_required: Optional[str] = None,
    ) -> bool:
        """
        Return True if this item may be added to the player's inventory.

        This basic check enforces the `movable` flag and an optional simple
        dependency like “you must already have X”.

        Parameters
        ----------
        user_items : list[Item]
            The player's current inventory.
        other_item_required : str or None, optional
            If provided, the player must already carry an item with this name.
        """
        if not self.movable:
            return False
        if not other_item_required:
            return True
        return any(x.name == other_item_required for x in user_items)



@dataclass
class Room:
    """
    A location the player can enter, inspect, and interact with.

    A `Room` bundles a short description, an item list, and two hook methods
    for custom behavior:
      - `run_story(...)` — executed when the player (re-)enters the room.
      - `enter_room(...)` — manages the room's input loop (inspect/leave/help).

    Parameters
    ----------
    name : str
        The display name of the room (e.g., "archive").
    description : str
        A brief description shown when the player enters the room.
    items_init : list[Item] or Item or None, optional
        Initial content of the room. You can pass a single `Item` or a list of items.
        Internally normalized to `self.items`.

    Attributes
    ----------
    name : str
        The display name.
    description : str
        The room's short description.
    visited : int
        How many times the player entered this room (starts at 0).
    items : list[Item]
        Current items visible in the room. Picking up an item removes it here.
    """

    name: str
    description: str
    items_init: Optional[List[Item] | Item] = None
    visited: int = 0
    items: List[Item] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        """Normalize `items_init` into the public `items` list."""
        if self.items_init is None:
            self.items = []
        elif isinstance(self.items_init, list):
            self.items = self.items_init[:]
        else:
            self.items = [self.items_init]

    def enter_room(self, user_items: List[Item], command_handler: CommandHandler) -> List[Item]:
        """
        Enter the room and run its interaction loop.

        Parameters
        ----------
        user_items : list[Item]
            The player's inventory (will be updated if items are taken).
        command_handler : CommandHandler
            Handles global commands like 'inventory', 'help', 'exit'.
        """
        self.visited += 1
        print(40 * "-")

        # Story hook
        user_items = self.run_story(user_items)

        while True:
            action = input(">> 'leave' to exit, 'inspect' to look around, 'help' for help: ").strip().lower()

            if command_handler.handle_global_commands(action):
                if not command_handler.game.game_active:
                    return user_items
                continue

            if action in {"leave", "exit room"}:
                print("You leave the room...")
                return user_items
            elif action in {"inspect", "look"}:
                user_items = self.show_items(user_items)
            else:
                print("Invalid command! Try 'inspect', 'leave', or 'help'.")

    def run_story(self, user_items: List[Item]) -> List[Item]:
        """
        Hook for room-specific story logic.

        Called every time the player enters the room (after the header/description
        and before the command loop). Use this to implement small events, puzzles,
        or state transitions (e.g., remove/add items, change the description, etc.).

        Parameters
        ----------
        user_items : list[Item]
            The player's current inventory.
        """
        print(f"You've entered the {self.name} {self.visited} time(s).")
        return user_items

    def show_items(self, user_items: List[Item]) -> List[Item]:
        """
        List visible items and let the player take movable ones.

        Iterates the current `self.items` list, prints each description, and for
        movable items asks the player if they want to take it. When taken, the
        item is appended to `user_items` and removed from `self.items`.

        Parameters
        ----------
        user_items : list[Item]
            The player's current inventory.
        """
        if not self.items:
            print("There is nothing of particular interest...")
            return user_items

        print("In here you find...")
        for item in self.items[:]:
            item.describe()
            if item.is_movable(user_items):
                while True:
                    action = input(f"Do you want to take {item.name}? (yes/no): ").strip().lower()
                    if action in {"yes", "y"}:
                        user_items.append(item)
                        self.items.remove(item)
                        print(f"You've taken the {item.name}.")
                        break
                    if action in {"no", "n"}:
                        print(f"You leave the {item.name} where it is.")
                        break
                    print("Please answer with yes or no!")
        return user_items

    def get_detail(self) -> str:
        """Return a one-line description of the room.

        Useful for quick 'look' commands or status overlays.
        """
        return f"You are in the {self.name}. {self.description}"



@dataclass
class Floor:
    """
    A collection of rooms and connections to other floors.

    A `Floor` models one level of the building (e.g., "cellar", "first floor")
    and acts as a map: it exposes room labels (for `enter <label>`) and
    directional exits to other floors (for `go <direction>` such as "up"/"down").

    Parameters
    ----------
    name : str
        The display name of the floor (e.g., "cellar").
    description : str
        A brief description of the area shown in the floor header.
    rooms : dict[str, Room], optional
        Mapping from a **room label** (the string the player types after `enter`)
        to a `Room` instance.
    connected_floors : dict[str, Floor], optional
        Mapping from a **direction** label (e.g., "up", "down") to another floor.

    Attributes
    ----------
    name : str
        The display name.
    description : str
        A short description used in the floor panel.
    rooms : dict[str, Room]
        Rooms accessible from this floor by label (e.g., "archive", "toilet").
    connected_floors : dict[str, Floor]
        Neighboring floors accessible by direction (e.g., "up" -> first floor).
    """

    name: str
    description: str
    rooms: Dict[str, Room] = field(default_factory=dict)
    connected_floors: Dict[str, "Floor"] = field(default_factory=dict)

    def add_room(self, direction: str, room: Room) -> None:
        """
        Register a room under a label the player can use with `enter`.

        Parameters
        ----------
        direction : str
            A symbolic room label (e.g., "archive", "toilet").
        room : Room
            The room instance to expose from this floor.
        """
        self.rooms[direction] = room

    def get_room(self, direction: str) -> Optional[Room]:
        """
        Retrieve a room by its label.

        Parameters
        ----------
        direction : str
            The room label originally used in `add_room`.
        """
        return self.rooms.get(direction)

    def add_connection(self, direction: str, floor: "Floor") -> None:
        """
        Connect this floor to another floor under a direction label.

        Parameters
        ----------
        direction : str
            A direction keyword the player can type after `go` (e.g., "up", "down").
        floor : Floor
            The neighboring floor to travel to.
        """
        self.connected_floors[direction] = floor

    def get_floor_in_direction(self, direction: str) -> Optional["Floor"]:
        """
        Get the neighboring floor for a given direction.

        Parameters
        ----------
        direction : str
            A direction keyword (e.g., "up", "down").
        """
        return self.connected_floors.get(direction)

    def get_orientation(self) -> str:
        """
        Build a readable list of options from this floor.
        """
        details = ""
        if self.rooms:
            for direction, room in self.rooms.items():
                details += f"\nType 'enter {direction}' to go to {room.name}."
        if self.connected_floors:
            for direction, floor in self.connected_floors.items():
                details += f"\nType 'go {direction}' to go to {floor.name}."
        return details

