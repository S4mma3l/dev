import reflex as rx
from dev.components.header_text import header_text

def calendar() -> rx.Component:
    return rx.vstack(
        header_text(
            "",
            "Wicked Nails"
        ),
        rx.vstack(
            rx.hstack(
                rx.text("hoy es: "),
                rx.text(id="countdown"),
                align_items="start"
            )
        ),
        rx.script(src="/dev/assets/js/date.js")
        
    )