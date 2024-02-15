import reflex as rx
import dev.styles.styles as styles
import dev.constants as constants
from dev.styles.fonts import Font
from dev.styles.styles import Size, Color, TextColor

def header() -> rx.Component:
    return rx.vstack(
         rx.button(
             rx.icon(tag="moon"),
             on_click=rx.toggle_color_mode,
             color=Color.TERCIARY.value,
         ),
        
        rx.heading(
            "Wicked Nails 2024",
            font= Font.DEFAULT.value,
            size="lg",
            padding_bottom=Size.DEFAULT.value,
            font_size=Size.BIGGER.value
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
                    rx.text("Para Todos"),
                    class_name="nes-container is-dark",
                    font_size=Size.BIG.value
                ),
                rx.span(
                    "Pagina de Nails ",
                    rx.span(
                        "Se Feliz ",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value  
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
                    "#nailsaddict",
                    href=constants.NAILS_HASHTAG,
                    is_external=True,
                    color=TextColor.TERCIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                ),
                
            ),
            flex_direction=["column", "column", "column", "row", "row"]
            
        ),
        padding_top=Size.BIGGER.value,
        style=styles.max_width_style,
        
    )
