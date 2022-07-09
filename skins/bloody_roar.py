from layouts import remotely_modern
from skins.colors import generic_buttons

original_buttons = {
    "punch": "#ef4729",
    "kick": "#5166b3",
    "beast": "#f7cb29",
    "guard": "#348eca",
}

wiki_buttons = {
    "punch": "#ffd905",
    "kick": "#22bc36",
    "beast": "#fe0d01",
    "guard": "#2637a8",
}

bloody_roar = {
    "default": {
        "button_a": original_buttons["kick"],
        "button_b": original_buttons["beast"],
        "button_x": original_buttons["punch"],
        "button_y": generic_buttons["white"],
        "l_bumper": generic_buttons["gray"],
        "r_bumper": original_buttons["guard"],
        "l_trigger": generic_buttons["gray"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
    "face_button_guard": {
        "button_a": original_buttons["kick"],
        "button_b": original_buttons["beast"],
        "button_x": original_buttons["punch"],
        "button_y": original_buttons["guard"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
    "wiki_default": {
        "button_a": wiki_buttons["kick"],
        "button_b": wiki_buttons["beast"],
        "button_x": wiki_buttons["punch"],
        "button_y": generic_buttons["white"],
        "l_bumper": generic_buttons["gray"],
        "r_bumper": wiki_buttons["guard"],
        "l_trigger": generic_buttons["gray"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
    "wiki_face_button_guard": {
        "button_a": wiki_buttons["kick"],
        "button_b": wiki_buttons["beast"],
        "button_x": wiki_buttons["punch"],
        "button_y": wiki_buttons["guard"],
        "l_bumper": generic_buttons["white"],
        "r_bumper": generic_buttons["gray"],
        "l_trigger": generic_buttons["white"],
        "r_trigger": generic_buttons["gray"],
        "variants": remotely_modern,
    },
}

