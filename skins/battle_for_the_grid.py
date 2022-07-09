from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "l": "#47f5e0",
    "m": "#2eb600",
    "h": "#d8cd29",
    "s": "#c10d01",
    "d": "#8d1ca1",
    "a": "#b87a00",
}

bftg = {
    "default": {
        "button_a": buttons["s"],
        "button_b": buttons["h"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": buttons["a"],
        "r_bumper": buttons["d"],
        "l_trigger": buttons["a"],
        "r_trigger": buttons["d"],
        "variants": remotely_modern,
    },
    "default_close_assist": {
        "button_a": buttons["s"],
        "button_b": buttons["h"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": buttons["d"],
        "r_bumper": buttons["a"],
        "l_trigger": buttons["d"],
        "r_trigger": buttons["a"],
        "variants": remotely_modern,
    },
    "anime": {
        "button_a": buttons["s"],
        "button_b": buttons["a"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": None,
        "r_bumper": buttons["h"],
        "l_trigger": None,
        "r_trigger": buttons["a"],
        "variants": remotely_modern,
    },
    "anime_8_button": {
        "button_a": buttons["s"],
        "button_b": buttons["a"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": buttons["a"],
        "r_bumper": buttons["h"],
        "l_trigger": buttons["d"],
        "r_trigger": buttons["d"],
        "variants": remotely_modern,
    },
    "anime_8_close_double": {
        "button_a": buttons["s"],
        "button_b": buttons["d"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": buttons["d"],
        "r_bumper": buttons["h"],
        "l_trigger": buttons["a"],
        "r_trigger": buttons["a"],
        "variants": remotely_modern,
    },
}
