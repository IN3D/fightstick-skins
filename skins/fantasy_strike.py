from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "attack": "#38b118",
    "special": "#fcc300",
    "jump": "#1e8bcc",
    "super": "#b46acb",
    "throw": "#fb9300",
}

fantasy_strike = {
    "default": {
        "button_a": buttons["jump"],
        "button_b": buttons["super"],
        "button_x": buttons["attack"],
        "button_y": buttons["special"],
        "l_bumper": None,
        "r_bumper": buttons["special"],
        "l_trigger": None,
        "r_trigger": buttons["throw"],
        "variants": remotely_modern,
    },
}
