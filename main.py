from os import system
from static import template
from manifest import manifest


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def button(value):
    if value is None:
        return "display: none;"
    else:
        return f"@include arcade-button({value});"

# TODO: unecessary, or re-purpose?
def layout_for_variant(variant):
    scss_keys = {
        'american': 'american',
        'astro_city': 'astro-city',
        'cluster_grid': 'cluster',
        'hori_slanted': 'hori-slanted',
        'hori_transitional': 'hori-transitional',
        'incline': 'incline',
        'lindbergh': 'lindbergh',
        'namco_noir': 'noir',
        'sega_p2': 'sega-p2',
        'viewlix': 'viewlix'
    }
    return scss_keys[variant]

def build_layouts():
    # TODO: write me!
    # originally the variation processing looked like this...
    # variants_for_skin = skin["variants"]
    # if variants_for_skin is not None:
    #     for variant in variants_for_skin:
    #         file_name = f"{set_dir}/{variant}.scss"
    #         layout = layout_for_variant(variant)
    #         processed_skin = {k: button(v) for k, v in skin.items()}
    #         props = processed_skin | { 'layout': layout, 'name': skin_set_name }
    #         with open(file_name, "w") as skin_file:
    #             skin_file.write(template.format(**props))
    return None

def build_skins():
    for skin_set_name, skin_set in manifest.items():
        print(f"Processing set: {bcolors.OKGREEN}{skin_set_name}{bcolors.ENDC}")

        set_dir = f"scss/{skin_set_name}"
        system(f"mkdir -p {set_dir}")

        for skin_name, skin in skin_set.items():
            file_name = f"{set_dir}/{skin_name}.scss"
            processed_skin = {k: button(v) for k, v in skin.items()}
            props = processed_skin | { 'set_name': skin_set_name, 'name': skin_set_name }
            with open(file_name, "w") as skin_file:
                skin_file.write(template.format(**props))

def run():
    # Delete all sub-directories in scss, i.e start over each run
    system("rm -rf ./scss/*/")
    print(f"{bcolors.BOLD}RUN STARTING...{bcolors.ENDC}")

    build_layouts()
    build_skins()



run()
