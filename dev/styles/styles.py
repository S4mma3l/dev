import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000PX"
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "1.5em"
    BUTTON = "2.25"
    BIGGER = "3em"
    SPECIAL = "16em"

STYLESHEETS = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css?family=Orbitron&display=swap",
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value,
    rx.heading: {
        "font_family": Font.DEFAULT.value,
        "color": TextColor.PRIMARY.value
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {
            "color": TextColor.ACCENT.value,
            "text_decoration": "none"
        } 
    },
    rx.Span: {
        "font_size": Size.BIG.value
    },
}

max_width_style = dict(
    align_items="start",
    padding_x=Size.BIG.value,
    width="100%",
    max_width=MAX_WIDTH
)