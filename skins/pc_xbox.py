from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "a": "#5ca935",
    "b": "#d41a25",
    "x": "#0084c4",
    "y": "#f1d100",
}

pc_xbox = {
    "4_button": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": buttons["x"],
        "button_y": buttons["y"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "6_button": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": buttons["x"],
        "button_y": buttons["y"],
        "l_bumper": None,
        "r_bumper": generic_buttons["gray"],
        "l_trigger": None,
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
    "8_button": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": buttons["x"],
        "button_y": buttons["y"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
}
