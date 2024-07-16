import reflex as rx 

from ..ui.base import base_page

# @rx.page(route='/about')
def users_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Users", size="9"),
            rx.text(
                "these are users",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)