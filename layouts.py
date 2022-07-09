# Includes everything except very specific layouts like the NeoGeo MVS
all_non_specific_layouts = [
    'american',
    'astro_city',
    'cluster_grid',
    'hori_slanted',
    'hori_transitional',
    'incline',
    'lindbergh',
    'namco_noir',
    'sega_p2',
    'viewlix'
]

# TODO: NOT IMPLEMENTED
# Just NeoGeo cabinet layouts
neogeo = ["mvs_slanted", "mvs_straight"]

hori_specific = ["hori_slanted", "hori_transitional"]

# Limits to layouts common from the late 80s to early 2000s
only_classic = [
    "american",
    "cluster_grid",
    "incline",
] + hori_specific

# Includes all layouts that are either new, or have hung around
only_modern = [
    "astro_city",
    "lindbergh",
    "namco_noir",
    "sega_p2",
    "viewlix"
]

# Modern, plus some older layouts that have hung around in limited capacities
remotely_modern = only_modern + hori_specific
