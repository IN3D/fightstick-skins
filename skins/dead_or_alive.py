from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "punch": "#f5b906",
    "kick": "#d50505",
    "hold": "#57bf05",
    "throw": "#3844c4",
    "special": "#ba15de",
}

doa = {
    "doa6": {
        "button_a": buttons["throw"],
        "button_b": buttons["kick"],
        "button_x": buttons["hold"],
        "button_y": buttons["punch"],
        "l_bumper": generic_buttons["gray"],
        "r_bumper": buttons["special"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
    "doa6_arcade_inspired": {
        "button_a": buttons["hold"],
        "button_b": buttons["throw"],
        "button_x": buttons["punch"],
        "button_y": buttons["kick"],
        "l_bumper": generic_buttons["gray"],
        "r_bumper": buttons["special"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["white"],
        "variants": remotely_modern,
    },
    # TODO: add more versions
    # Pretty sure "special" is new in 6, so it's no use to older versions
    # and the arcade original was very different
}
