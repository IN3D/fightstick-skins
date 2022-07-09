template = """// {name} - {layout}
@import "../../arcade_button.scss";
@import "../../globals.scss";

.controller.fight-stick {{
    background: none;

    .arrows {{ display: none; }}
    .quadrant {{ display: none; }}

    .abxy {{
        bottom: ${layout}-abxy-bottom;
        left: ${layout}-abxy-left;

        .button {{
            &.a {{
                {button_a}
                left: ${layout}-a-left;
                bottom: ${layout}-a-bottom;
            }}
            &.b {{
                {button_b}
                right: ${layout}-b-right;
                bottom: ${layout}-b-bottom;
            }}
            &.x {{ {button_x} }} /* anchor point */
            &.y {{
                {button_y}
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
                {l_trigger}
                bottom: ${layout}-l-trigger-bottom;
                right: ${layout}-l-trigger-right;
            }}
            &.right {{ {r_trigger} }} /* anchor */
        }}
    }}

    .bumpers {{
        right: ${layout}-bumpers-right;
        top: ${layout}-bumpers-top;

        .bumper {{
            &.left {{
                {l_bumper}
                bottom: ${layout}-l-bumper-bottom;
                right: ${layout}-l-bumper-right;
            }}
            &.right {{ {r_bumper} }} /* anchor */
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

