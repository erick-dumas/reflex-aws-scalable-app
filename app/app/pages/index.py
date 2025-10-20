import reflex as rx
from app.components import sidebar

@rx.page("/")
def dashboard() -> rx.Component:
    return rx.box(
        sidebar(),
        rx.box(
            rx.text("Main Dashboard Content"),

            # Properties for the main content area
            margin_left="25em",
            padding="2em",
        )
    )