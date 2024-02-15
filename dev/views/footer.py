import reflex as rx
import dev.styles.styles as styles
import dev.constants as constants
from dev.styles.styles import Size
from dev.styles.colors import TextColor

def footer() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Lorena Garrido Campos. Manicurista Profesional",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.SMALL.value
                
            ),
            rx.link(
                "Creada Con  ",
                rx.box(class_name="nes-icon is-small heart"),
                "  para Mis Clientas.",
                href=constants.INSTAGRAM_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.SECONDARY.value
                
            ),
            align_items="center",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="wickednails.png",
            alt="logo wickednails",
            class_name="nes-avatar is-large"
        ),
        padding_botton= Size.BIG.value,
        style=styles.max_width_style
        
    )