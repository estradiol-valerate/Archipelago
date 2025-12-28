from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from . import songs
from .items import get_item_count

if TYPE_CHECKING:
    from .world import UNBEATABLEArcadeWorld


def set_all_rules(world: UNBEATABLEArcadeWorld) -> None:
    return