from layouts import remotely_modern, only_classic, all_non_specific_layouts
from skins.colors import generic_buttons

buttons = {
    "lk": "#d41a25", # red
    "lp": "#f1d100", # yellow
    "rk": "#0084c4", # blue
    "rp": "#5ca935", # green
}

black_button = "#444444"

tekken = {
    "tekken_1": {
        "button_a": buttons["lk"],
        "button_b": buttons["rk"],
        "button_x": buttons["lp"],
        "button_y": buttons["rp"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": only_classic,
    },
    "classic": {
        "button_a": buttons["lk"],
        "button_b": buttons["lk"],
        "button_x": buttons["lp"],
        "button_y": buttons["lp"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts,
    },
    "classic_inverted": {
        "button_a": buttons["lp"],
        "button_b": buttons["lp"],
        "button_x": buttons["lk"],
        "button_y": buttons["lk"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts,
    },
    "black_n_white": {
        "button_a": black_button,
        "button_b": generic_buttons["white"],
        "button_x": black_button,
        "button_y": generic_buttons["white"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts
    },
    "operators_special": {
        "button_a": generic_buttons["white"],
        "button_b": buttons["lp"],
        "button_x": "#e5553b", # orange
        "button_y": buttons["lk"],
        "l_bumper": None,
        "r_bumper": None,
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts,
    },
    "tag_original": {
        "button_a": buttons["rk"],
        "button_b": buttons["lk"],
        "button_x": black_button,
        "button_y": buttons["lp"],
        "l_bumper": None,
        "r_bumper": buttons["rp"],
        "l_trigger": None,
        "r_trigger": None,
        "variants": all_non_specific_layouts,
    },
}
