import reflex as rx

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.card(rx.text("Sidebar Content 1 ")),
            rx.card(rx.text("Sidebar Content 2 ")),
            width="100%",
            spacing="2",
            direction="column",
        ),

        # Properties for the sidebar container
        width="25em",
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        padding="2em",
        background_color="rgba(255, 255, 255, 0.8)", 
        backdrop_filter="blur(10px)",
    )