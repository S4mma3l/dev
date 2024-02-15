import reflex as rx
import dev.constants as constants
from dev.styles.styles import Size, Color
from dev.components.link_icon import link_icon


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="wickednails.png",
                alt="logo de wicked nails",
                width=Size.BIGGER.value,
                height=Size.BIGGER.value
            ),  
            rx.text("Wicked Nails"),
            rx.spacer(),
            link_icon(
                "instagram",
                constants.INSTAGRAM_URL
            ),
            width="100%",
            font_size=Size.BIG.value
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.50em solid {Color.SECONDARY.value}",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.DEFAULT.value,
        z_index="700",
        top="0",
        
    )
