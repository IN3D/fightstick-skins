from layouts import remotely_modern
from skins.colors import generic_buttons


buttons = {
    "a": "#52af56",
    "b": "#d572b2",
    "skill": "#e9bf51",
    "mana_skill": "#7194e8",
    "guard": "#62c5da",
    "awakening": "#e04d55",
}

dnf = {
    "type_a": {
        "button_a": buttons["mana_skill"],
        "button_b": buttons["skill"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": generic_buttons["white"],
        "l_trigger": buttons["awakening"],
        "r_trigger": buttons["guard"],
        "variants": remotely_modern,
    },
    "type_b": {
        "button_a": buttons["mana_skill"],
        "button_b": None,
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": buttons["guard"],
        "r_bumper": buttons["skill"],
        "l_trigger": buttons["awakening"],
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "type_b_full": {
        "button_a": buttons["mana_skill"],
        "button_b": generic_buttons["white"],
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": buttons["guard"],
        "r_bumper": buttons["skill"],
        "l_trigger": buttons["awakening"],
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
}