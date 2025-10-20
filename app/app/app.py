import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    return rx.text("reflex aws app")


app = rx.App()
app.add_page(index)
