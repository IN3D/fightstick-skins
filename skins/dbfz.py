from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "l": "#0ed1f2",
    "m": "#03c214",
    "h": "#ffde0d",
    "s": "#f61919",
    "a": "#e57239",
}

dbfz = {
    "default": {
        "button_a": buttons["s"],
        "button_b": buttons["h"],
        "button_x": buttons["l"],
        "button_y": buttons["m"],
        "l_bumper": buttons["a"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": buttons["a"],
        "r_trigger": generic_buttons["gray"],
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
        "l_bumper": generic_buttons["white"],
        "r_bumper": buttons["h"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": buttons["a"],
        "variants": remotely_modern,
    },
}
