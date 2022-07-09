from layouts import remotely_modern
from skins.colors import generic_buttons

buttons = {
    "a": "#e500b0f",
    "b": "#1586bf",
    "c": "#27a56a",
    "d": "#e0e544",
}

tag_buttons = {
    "a": "#f26bff",
    "b": "#17e40c",
    "c": "#ff2b0d",
    "d": "#137cff",
    "tag": "#ffd209",
}

wiki_buttons = {
    "a": "#02bdf2",
    "b": "#007fc3",
    "c": "#184fa1",
    "d": "#d7642e",
    "tag": "#f57bea",
}

blazblue = {
    "type_1": {
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
    "type_2": {
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
    "cross_tag_type_2": {
        "button_a": tag_buttons["d"],
        "button_b": None,
        "button_x": tag_buttons["a"],
        "button_y": tag_buttons["b"],
        "l_bumper": None,
        "r_bumper": tag_buttons["c"],
        "l_trigger": None,
        "r_trigger": tag_buttons["tag"],
        "variants": remotely_modern,
    },
}
