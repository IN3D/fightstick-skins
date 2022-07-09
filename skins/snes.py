from layouts import all_non_specific_layouts
from skins.colors import generic_buttons

buttons = {
    "light_purple": "#a099d4",
    "dark_purple": "#4d2a81",
    "controller": "#c8c6d1", # bumpers are the same color as controller body
}

snes = {
    "4_button": {
        "button_a": buttons["dark_purple"],
        "button_b": buttons["dark_purple"],
        "button_x": buttons["light_purple"],
        "button_y": buttons["light_purple"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts,
    },
    "6_button": {
        "button_a": buttons["dark_purple"],
        "button_b": buttons["dark_purple"],
        "button_x": buttons["light_purple"],
        "button_y": buttons["light_purple"],
        "l_bumper": None,
        "r_bumper": buttons["controller"],
        "l_trigger": None,
        "r_trigger": buttons["controller"],
        "variants": all_non_specific_layouts,
    },
    "8_button": {
        "button_a": buttons["dark_purple"],
        "button_b": buttons["dark_purple"],
        "button_x": buttons["light_purple"],
        "button_y": buttons["light_purple"],
        "l_bumper": buttons["controller"],
        "r_bumper": buttons["controller"],
        "l_trigger": buttons["controller"],
        "r_trigger": buttons["controller"],
        "variants": all_non_specific_layouts,
    },
}
