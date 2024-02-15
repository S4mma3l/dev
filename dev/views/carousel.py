import reflex as rx
from dev.styles.styles import Size
import dev.styles.styles as styles

def cards() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.image(
                src="nails1.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails2.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails1.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails2.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails2.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails1.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            rx.image(
                src="nails2.png",
                alt="Clienta unas",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value
            ),
            align_items="center",
            width="100%",
            font_size=Size.SMALL.value,
        ),
        style=styles.max_width_style
    )


    
