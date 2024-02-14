import reflex as rx

def link_icon(icon: str, url: str) -> rx.Component:
    return rx.link(
        "",
        class_name="nes-icon instagram is-medium",
        href=url,
        is_external=True
    )