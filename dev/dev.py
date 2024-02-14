import reflex as rx
import dev.styles.styles as styles
from dev.styles.styles import Size
from dev.views.navbar import navbar
from dev.views.header import header

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                header(),
                header(),
                header(),
                width="100%",
                spacing=Size.BIGGER.value
            )
        )    
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    padding_x=Size.BIG.value,
    width="100%",
    style=styles.BASE_STYLE

)

app.add_page(
    index,
    title="Wicked Nails",
    description="Un Encanto en Tus Unas"
)
