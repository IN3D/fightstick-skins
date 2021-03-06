from layouts import all_non_specific_layouts, only_classic, remotely_modern
from skins.colors import generic_buttons, capcom_classic


third_strike_alt = {
    "yellow": "#ffdf19",
    "green": "#007d42",
    "red": "#ce2f16",
    "black": "#2e2e38",
}

sf4 = {
    "blue": "#22a4e5",
    "yellow": "#eddf23",
    "red": "#e53a2d",
}

sf5 = {
    "lp": "#e5d085",
    "mp": "#f2c500",
    "hp": "#f39800",
    "lk": "#95cae5",
    "mk": "#54bce5",
    "hk": "#00a3ea",
}

street_fighter = {
    "sf3_marvel_like": {
        "button_a": capcom_classic["red"],
        "button_b": capcom_classic["green"],
        "button_x": capcom_classic["red"],
        "button_y": capcom_classic["green"],
        "l_bumper": None,
        "r_bumper": capcom_classic["blue"],
        "l_trigger": None,
        "r_trigger": capcom_classic["blue"],
        "variants": only_classic,
    },
    "sf3_marvel_alt": {
        "button_a": capcom_classic["red"],
        "button_b": capcom_classic["blue"],
        "button_x": capcom_classic["red"],
        "button_y": capcom_classic["blue"],
        "l_bumper": None,
        "r_bumper": capcom_classic["green"],
        "l_trigger": None,
        "r_trigger": capcom_classic["green"],
        "variants": only_classic,
    },
    "sf3_ygblk": {
        "button_a": third_strike_alt["yellow"],
        "button_b": third_strike_alt["green"],
        "button_x": third_strike_alt["yellow"],
        "button_y": third_strike_alt["green"],
        "l_bumper": None,
        "r_bumper": third_strike_alt["black"],
        "l_trigger": None,
        "r_trigger": third_strike_alt["black"],
        "variants": only_classic,
    },
    "sf3_rasta": {
        "button_a": third_strike_alt["green"],
        "button_b": third_strike_alt["yellow"],
        "button_x": third_strike_alt["green"],
        "button_y": third_strike_alt["yellow"],
        "l_bumper": None,
        "r_bumper": third_strike_alt["red"],
        "l_trigger": None,
        "r_trigger": third_strike_alt["red"],
        "variants": all_non_specific_layouts,
    },
    "sf3_rasta_alt": {
        "button_a": third_strike_alt["yellow"],
        "button_b": third_strike_alt["green"],
        "button_x": third_strike_alt["yellow"],
        "button_y": third_strike_alt["green"],
        "l_bumper": None,
        "r_bumper": third_strike_alt["red"],
        "l_trigger": None,
        "r_trigger": third_strike_alt["red"],
        "variants": all_non_specific_layouts,
    },
    "sf4": {
        "button_a": sf4["blue"],
        "button_b": sf4["yellow"],
        "button_x": sf4["blue"],
        "button_y": sf4["yellow"],
        "l_bumper": None,
        "r_bumper": sf4["red"],
        "l_trigger": None,
        "r_trigger": sf4["red"],
        "variants": all_non_specific_layouts,
    },
    "sf4_full": {
        "button_a": sf4["blue"],
        "button_b": sf4["yellow"],
        "button_x": sf4["blue"],
        "button_y": sf4["yellow"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": sf4["red"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": sf4["red"],
        "variants": all_non_specific_layouts,
    },
    "sf5": {
        "button_a": sf5["lk"],
        "button_b": sf5["mk"],
        "button_x": sf5["lp"],
        "button_y": sf5["mp"],
        "l_bumper": None,
        "r_bumper": sf5["hp"],
        "l_trigger": None,
        "r_trigger": sf5["hk"],
        "variants": remotely_modern,
    },
    "sf5_full": {
        "button_a": sf5["lk"],
        "button_b": sf5["mk"],
        "button_x": sf5["lp"],
        "button_y": sf5["mp"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": sf5["hp"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": sf5["hk"],
        "variants": remotely_modern,
    },
}
