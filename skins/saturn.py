from layouts import remotely_modern
from skins.colors import generic_buttons


buttons = {
    "a": "#3a9154",
    "b": "#ffd800",
    "c": "#1f34a8",
    "bumper": "#a80048",
}

saturn = {
    "default": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": generic_buttons["gray"],
        "button_y": generic_buttons["gray"],
        "l_bumper": None,
        "r_bumper": generic_buttons["gray"],
        "l_trigger": None,
        "r_trigger": buttons["c"],
        "variants": remotely_modern,
    },
    "default_only_abc": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": None,
        "button_y": None,
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": buttons["c"],
        "variants": remotely_modern,
    },
    "default_w_bumpers": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": generic_buttons["gray"],
        "button_y": generic_buttons["gray"],
        "l_bumper": buttons["bumper"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": buttons["bumper"],
        "r_trigger": buttons["c"],
        "variants": remotely_modern,
    },
}


