from layouts import all_non_specific_layouts, only_classic, remotely_modern
from skins.colors import generic_buttons

capcom_usa_buttons = {
    "red": "#e2350a",
    "white": generic_buttons["white"],
    "blue": "#3368cc",
}

street_fighter = {
    "capcom_usa": {
        "button_a": capcom_usa_buttons["red"],
        "button_b": capcom_usa_buttons["white"],
        "button_x": capcom_usa_buttons["red"],
        "button_y": capcom_usa_buttons["white"],
        "l_bumper": None,
        "r_bumper": capcom_usa_buttons["blue"],
        "l_trigger": None,
        "r_trigger": capcom_usa_buttons["blue"],
        "variants": only_classic,
    },
    "capcom_usa_alt": {
        "button_a": capcom_usa_buttons["red"],
        "button_b": capcom_usa_buttons["blue"],
        "button_x": capcom_usa_buttons["red"],
        "button_y": capcom_usa_buttons["blue"],
        "l_bumper": None,
        "r_bumper": capcom_usa_buttons["white"],
        "l_trigger": None,
        "r_trigger": capcom_usa_buttons["white"],
        "variants": only_classic,
    },
    "sf2_rando_cab": {
        "button_a": "#1fc365",
        "button_b": "#444444",
        "button_x": "#e2350a",
        "button_y": "#128ac7",
        "l_bumper": None,
        "r_bumper": "#fa9060",
        "l_trigger": None,
        "r_trigger": "#f4d11f",
        "variants": only_classic,
    },
}
