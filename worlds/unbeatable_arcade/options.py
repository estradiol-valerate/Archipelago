from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class TargetRating(Range):
    """
    The star rating you need to achieve to complete the randomizer.
    You should set this to just a bit lower than the rating you have right now.
    """

    display_name = "Target Rating"

    range_start = 2
    range_end = 13

    default = 5


class UseBreakout(Toggle):
    """
    Enables songs included in UNBEATABLE - Breakout Edition.
    This requires that you own the UNBEATABLE - Breakout Edition Upgrade DLC and have it installed.
    """

    display_name = "Include Breakout Songs"


class MinDifficulty(Choice):
    """
    Sets the first unlocked difficulty. Lower difficulties than this will be inacessible.
    Higher difficulties must be unlocked by finding 'Progressive Difficulty' items.
    The more difficulties there are between this and what you need to reach your rating goal,
    the longer the game will generally be.
    (Star difficulty is not available because some songs have none)
    """

    display_name = "Minimum Difficulty"

    option_beginner = 0
    option_normal = 1
    option_hard = 2
    option_expert = 3
    option_unbeatable = 4

    default = option_beginner


class StartSongCount(Range):
    """
    Sets how many songs to start with.
    """

    display_name = "Starting Songs"

    range_start: 1
    range_end: 10
    
    default: 2


@dataclass
class UNBEATABLEArcadeOptions(PerGameCommonOptions):
    target_rating: TargetRating
    use_breakout: UseBreakout
    min_difficulty: MinDifficulty
    start_song_count: StartSongCount