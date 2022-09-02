template = """// {set_name} - {name}
@import "../arcade_button.scss";
@import "../border.scss";
@import "../button_defaults.scss";
@import "../globals.scss";

.controller.fight-stick {{
    background: none;

    .arrows {{ display: none; }}
    .quadrant {{ display: none; }}

    .abxy {{
        .button {{
            @include button-defaults();

            &.a {{ {button_a} }}
            &.b {{ {button_b} }}
            &.x {{ {button_x} }} /* anchor point */
            &.y {{ {button_y} }}
        }}
    }}

    .triggers {{
        .trigger-button {{
            @include button-defaults();

            &.left {{ {l_trigger} }}
            &.right {{ {r_trigger} }} /* anchor */
        }}
    }}

    .bumpers {{
        .bumper {{
            @include button-defaults();

            &.left {{ {l_bumper} }}
            &.right {{ {r_bumper} }} /* anchor */
        }}
    }}
}}
""" 


layouts_template = """
.controller.fight-stick {{
    .abxy {{
        bottom: ${layout}-abxy-bottom;
        left: ${layout}-abxy-left;

        .button {{
            &.a {{
                left: ${layout}-a-left;
                bottom: ${layout}-a-bottom;
            }}
            &.b {{
                right: ${layout}-b-right;
                bottom: ${layout}-b-bottom;
            }}
            /* x intentionally omitted */
            &.y {{
                right: ${layout}-y-right;
                top: ${layout}-y-top;
            }}
        }}
    }}

    .triggers {{
        right: ${layout}-triggers-right;
        top: ${layout}-triggers-top;

        .trigger-button {{
            &.left {{
                bottom: ${layout}-l-trigger-bottom;
                right: ${layout}-l-trigger-right;
            }}
            /* right intentionally omitted */
        }}
    }}

    .bumpers {{
        right: ${layout}-bumpers-right;
        top: ${layout}-bumpers-top;

        .bumper {{
            &.left {{
                bottom: ${layout}-l-bumper-bottom;
                right: ${layout}-l-bumper-right;
            }}
            /* right intentionally omitted */
        }}
    }}

    .fight-stick {{
        .fstick {{
            top: ${layout}-fstick-top;
            left: ${layout}-fstick-left;
        }}
    }}
}}
"""