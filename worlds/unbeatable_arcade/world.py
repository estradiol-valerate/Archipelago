from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items

class UNBEATABLEArcadeWorld(World):
    """
    UNBEATABLE is a rhythm game where music is illegal and you do crimes.
    UNBEATABLE Arcade Mode is a gamemode separate from the story mode, where you can play songs from the game (and other places) to your heart's content.
    """

    game = "UNBEATABLE Arcade"

    def create_regions(self) -> None:
        return

    def set_rules(self) -> None:
        return
    
    def create_items(self) -> None:
        return
    
    def create_item(self) -> items.UNBEATABLEArcadeItem:
        return items.UNBEATABLEArcadeItem()

    def get_filler_item_name(self) -> str:
        return ""

    def fill_slot_data(self) -> Mapping[str, Any]:
        return []