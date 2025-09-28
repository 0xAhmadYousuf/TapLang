# TapLang Specification Data
# Authoritative data source for TapLang interpreter
# 🤖 Designed primarily for AI agents and automation systems
# Converted from JSON for better Python performance

SPEC = {
    "language": {
        "name": "TapLang",
        "version": "1.0.0",
        "description": "Keyboard action language for AI systems",
        "case_sensitive": False
    },
    "instructions": {
        "CLICK": "Press and release key",
        "PRESS": "Press and hold key",
        "RELEASE": "Release held key",
        "TYPE": "Type text or random selection",
        "WAIT": "Wait milliseconds",
        "SET_WAIT": "Set wait time or random range",
        "FUNCTION": "Press function key F1-F12",
        "PRESS_LEFT": "Press left side modifier",
        "PRESS_RIGHT": "Press right side modifier",
        "ESCAPE_TYPE_START": "Begin escape sequence",
        "ESCAPE_TYPE_END": "End escape sequence"
    },
    "keys": {
        "letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "numbers": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "symbols": [",", ".", ";", "'", "/", "\\", "[", "]", "-", "=", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?"],
        "special": ["ENTER", "SPACE", "TAB", "BACKSPACE", "DELETE", "ESC", "INSERT", "HOME", "END", "PAGE_UP", "PAGE_DOWN", "CAPS_LOCK", "NUM_LOCK", "SCROLL_LOCK", "PRINT_SCREEN", "PAUSE"],
        "arrows": ["UP", "DOWN", "LEFT", "RIGHT"],
        "modifiers": ["SHIFT", "CTRL", "ALT", "WIN", "CMD", "META"],
        "function_keys": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    },
    "rules": {
        "press_release": "Every PRESS, PRESS_LEFT, or PRESS_RIGHT must have matching RELEASE",
        "case_insensitive": "All instructions and keys are case-insensitive",
        "escape_sequence": "Use ESCAPE_TYPE_START and ESCAPE_TYPE_END for text with keywords",
        "set_wait": "SET_WAIT[n] sets default wait time, SET_WAIT[RANDOM[min,max]] sets random range",
        "type_random": "TYPE supports RANDOM[option1,option2,option3] for random text selection"
    },
    "examples": {
        "basic": "TYPE[Hello] CLICK[SPACE] TYPE[World]",
        "function": "FUNCTION[1] FUNCTION[12]",
        "modifier": "PRESS_LEFT[SHIFT] CLICK[A] RELEASE[SHIFT]",
        "symbols": "CLICK[!] CLICK[@] CLICK[#]",
        "escape": "ESCAPE_TYPE_START[Text with PRESS[SHIFT] and CLICK[A] keywords] ESCAPE_TYPE_END[~]",
        "press_rule": "PRESS[CTRL] CLICK[C] RELEASE[CTRL]",
        "set_wait_fixed": "SET_WAIT[500] WAIT[] WAIT[] TYPE[Done]",
        "set_wait_random": "SET_WAIT[RANDOM[100,1000]] WAIT[] WAIT[] TYPE[Random delays]",
        "type_random": "TYPE[RANDOM[Hello,Hi,Hey]] WAIT[500] TYPE[RANDOM[World,Universe,Earth]]"
    }
}

# Build valid keys set from spec
VALID_KEYS = set()
for category in SPEC["keys"].values():
    VALID_KEYS.update([key.upper() for key in category])

VALID_INSTRUCTIONS = set(SPEC["instructions"].keys())

def get_spec():
    """Get the specification dictionary"""
    return SPEC

def get_valid_keys():
    """Get set of valid keys"""
    return VALID_KEYS

def get_valid_instructions():
    """Get set of valid instructions"""
    return VALID_INSTRUCTIONS