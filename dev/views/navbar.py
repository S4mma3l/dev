import reflex as rx
from dev.styles.styles import Size


def navbat() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="wickednails.png",
                alt="logo de wicked nails",
                width=Size.BIGGER.value,
                height=Size.BIGGER.value
            ),

            rx.text("Wicked Nails")
        )
    )
