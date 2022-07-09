from layouts import remotely_modern
from skins.colors import generic_buttons


buttons = {
    "a": "#02bdf2",
    "b": "#007fc3",
    "c": "#184fa1",
    "d": "#d7642e",
    "tag": "#f57bea",
}

dustloop = {
    "type_1": {
        "button_a": buttons["a"],
        "button_b": None,
        "button_x": buttons["b"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": buttons["d"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "type_1_5_button_pinky": {
        "button_a": buttons["a"],
        "button_b": None,
        "button_x": buttons["b"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": buttons["d"],
        "l_trigger": None,
        "r_trigger": buttons["tag"],
        "variants": remotely_modern,
    },
    "type_1_6_button_pinky": {
        "button_a": buttons["a"],
        "button_b": generic_buttons["white"],
        "button_x": buttons["b"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": buttons["d"],
        "l_trigger": None,
        "r_trigger": buttons["tag"],
        "variants": remotely_modern,
    },
    "type_1_5_button_thumb": {
        "button_a": buttons["a"],
        "button_b": buttons["tag"],
        "button_x": buttons["b"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": buttons["d"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "type_1_6_button_thumb": {
        "button_a": buttons["a"],
        "button_b": buttons["tag"],
        "button_x": buttons["b"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": buttons["d"],
        "l_trigger": None,
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
    "wiki_type_2": {
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
    "type_2_5_button_pinky": {
        "button_a": buttons["d"],
        "button_b": None,
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": buttons["tag"],
        "variants": remotely_modern,
    },
    "type_2_6_button_pinky": {
        "button_a": buttons["d"],
        "button_b": generic_buttons["white"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": buttons["tag"],
        "variants": remotely_modern,
    },
    "type_2_5_button_thumb": {
        "button_a": buttons["d"],
        "button_b": buttons["tag"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "type_2_6_button_thumb": {
        "button_a": buttons["d"],
        "button_b": buttons["tag"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": None,
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
}