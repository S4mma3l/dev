import reflex as rx
import dev.constants as constants
import dev.styles.styles as styles
from dev.styles.styles import TextColor, Size
from dev.components.button import button


def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "¿Cómo agendar una cita?",
                class_name="title",
                color=TextColor.ACCENT.value,
                font_size=Size.MEDIUM.value
            ),
            rx.span(
                rx.box(class_name="nes-icon trophy is-small"),
                " Escribeme al Whatsapp."),
            rx.span(
                rx.box(class_name="nes-icon trophy is-small"),
                " Indicame el dia y la hora."),
            rx.span(
                rx.box(class_name="nes-icon trophy is-small"),
                " Enviame Tu Diseño, Por Favor!"),
            rx.span(
                rx.box(class_name="nes-icon trophy is-small"),
                " Confirmare Tu Cita, Nos Vemos Pronto."
            ),
            rx.span(
                rx.box(class_name="nes-icon trophy is-small"),
                " Recuerda Siempre dejar tu Reseñas en mis redes, estare muy Agradecida."
            ),
             button(
                "Instagram",
                constants.INSTAGRAM_URL
            ),
            class_name="nes-container is-dark with-title is-centered",
            align_items="center",
            width="100%",
            font_size=Size.SMALL.value,
        ),
        style=styles.max_width_style
    )