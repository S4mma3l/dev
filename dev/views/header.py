import reflex as rx
import dev.styles.styles as styles
from dev.styles.fonts import Font
from dev.styles.styles import Size, Color, TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Wicked Nails 2024",
            font= Font.DEFAULT.value,
            size="lg",
            padding_bottom=Size.DEFAULT.value
        ),
        rx.flex(
            rx.image(
                src="wickednails.png",
                alt="imagen logo",
                width=Size.SPECIAL.value,
                height=Size.SPECIAL.value,
                margin_right=Size.BIG.value   
            ),
            rx.vstack(
                rx.box(
                    rx.text("Feliz Dia"),
                    rx.text("Para Todos")
                ),
                rx.span(
                    "Pagina de Nails ",
                    rx.span(
                        "Se Feliz ",
                        color=TextColor.ACCENT.value    
                    ),
                    ";-)"
                ),
                rx.span(
                    "Como Estas?"
                ),
                rx.span(
                    "Sera Genial!!"
                ),
                rx.link(
                    "Vuelve Pronto!!",
                    href="",
                    is_external=True,
                    color=TextColor.TERCIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                ),
                align_items="start",
            ),
            flex_direction=["column", "column", "column", "row", "row"]
            
        ),
        padding_top=Size.BIGGER.value,
        style=styles.max_width_style
           
    )