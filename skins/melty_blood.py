from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "a": "#eb188b",
    "b": "#ed7d0c",
    "c": "#178de5",
    "d": "#2aca74",
}

melty_blood = {
    "default": {
        "button_a": buttons["d"],
        "button_b": None,
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "6_button": {
        "button_a": buttons["d"],
        "button_b": generic_buttons["white"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
    "8_button": {
        "button_a": buttons["d"],
        "button_b": generic_buttons["white"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": generic_buttons["gray"],
        "r_bumper": buttons["c"],
        "l_trigger": generic_buttons["gray"],
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
}
