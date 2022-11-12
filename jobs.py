from enum import Enum

class Jobs(Enum):
    WARRIOR = 1
    WIZARD = 2
    HEALER = 3
    THIEF = 4
    MAGICKNIGHT = 5 # WARRIOR x WIZARD
    HOLYKNIGHT = 6  # WARRIOR x HEALER
    ASSASSIN = 7    # WARRIOR x THIEF
    PRIEST = 8      # WIZARD  x HEALER
    ELEMENTALOR = 9 # WIZARD  x THIEF
    ALCHEMIST = 10  # HEALER  x THIEF