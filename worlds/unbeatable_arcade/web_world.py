from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class UNBEATABLEArcadeWebWorld(WebWorld):
    game = "UNBEATABLE Arcade"

    theme = "partyTime"

    tutorials = [
        Tutorial(
            tutorial_name="Setup Guide",
            description="A guide to setting up unbeatAP for Arcade Mode.",
            language="English",
            file_name="guide_en.md",
            link="guide/en",
            authors=["AllPoland"]
        )
    ]