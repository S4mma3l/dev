import reflex as rx
import dev.styles.styles as styles


def index() -> rx.Component:
    return rx.box(
        

    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE

)

app.add_page(
    index,
    title="Wicked Nails",
    description="Un Encanto en Tus Unas"
)
