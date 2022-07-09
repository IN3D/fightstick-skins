from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "a": "#cc3939",
    "b": "#eac12e",
    "c": "#3eb23a",
    "d": "#33a8cc",
}

neogeo = {
    "neopad": {
        "button_a": buttons["a"],
        "button_b": buttons["b"],
        "button_x": buttons["c"],
        "button_y": buttons["d"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "kof": {
        "button_a": buttons["b"],
        "button_b": buttons["d"],
        "button_x": buttons["a"],
        "button_y": buttons["c"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "classic_curve": {
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
    "classic_curve_bottom_d": {
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
    "classic_straight": {
        "button_a": None,
        "button_b": None,
        "button_x": buttons["a"],
        "button_y": buttons["b"],
        "l_bumper": buttons["d"],
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
    "classic_ex": {
        "button_a": buttons["a"],
        "button_b": None,
        "button_x": None,
        "button_y": buttons["b"],
        "l_bumper": buttons["d"],
        "r_bumper": buttons["c"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": remotely_modern,
    },
}
