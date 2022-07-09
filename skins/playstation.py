from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "cross": "#92a7d6",
    "circle": "#ff5a34",
    "square": "#e791c2",
    "triangle": "#01ba9b",
}

playstation = {
    "4_button": {
        "button_a": buttons["cross"],
        "button_b": buttons["circle"],
        "button_x": buttons["square"],
        "button_y": buttons["triangle"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "6_button": {
        "button_a": buttons["cross"],
        "button_b": buttons["circle"],
        "button_x": buttons["square"],
        "button_y": buttons["triangle"],
        "l_bumper": None,
        "r_bumper": generic_buttons["gray"],
        "l_trigger": None,
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
    "8_button": {
        "button_a": buttons["cross"],
        "button_b": buttons["circle"],
        "button_x": buttons["square"],
        "button_y": buttons["triangle"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
}
