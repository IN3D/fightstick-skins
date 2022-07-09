from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "lp": "#d8b038",
    "mp": "#d66331",
    "hp": "#ca2e2a",
    "lk": "#7dc1cd",
    "mk": "#2c5fb2",
    "hk": "#702fbf",
}

skullgirls = {
    "default": {
        "button_a": buttons["lk"],
        "button_b": buttons["mk"],
        "button_x": buttons["lp"],
        "button_y": buttons["mp"],
        "l_bumper": None,
        "r_bumper": buttons["hp"],
        "l_trigger": None,
        "r_trigger": buttons["hk"],
        "variants": remotely_modern,
    },
    "8_button": {
        "button_a": buttons["lk"],
        "button_b": buttons["mk"],
        "button_x": buttons["lp"],
        "button_y": buttons["mp"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": buttons["hp"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": buttons["hk"],
        "variants": remotely_modern,
    },
}
